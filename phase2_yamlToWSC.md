# Pointer-Safe Translation Workflow for WSC Script Modification
## #️⃣ Overview

The WSC engine used in this game stores script data in a binary opcode-based format that depends heavily on:

- fixed byte offsets
- length-prefixed strings
- tightly packed parameters

Because of this, inserting longer translated text directly into the original .wsc file will corrupt all offsets and crash the game.

To avoid full reverse-engineering (Option A), this project uses Option B: Pointer-Based Translation Injection, which keeps the WSC binary structure intact while redirecting string lookups to an external table.

This allows:

✔ arbitrary-length translations
✔ no offset shifting
✔ safe patching
✔ reversible & testable modifications

## #️⃣ 2. Why We Cannot Patch the WSC Directly

WSC blocks look like:

```json
<0000018E:000001C9>
夏が終わった――\nそう実感した瞬間はいつだっただろう？%K%P
```

If the English text is longer than Japanese:
1. offsets move
2. jump targets break
3. parsing tables become invalid
4. game freezes or immediately closes

➡ Direct replacement is unsafe.


## #️⃣ 3. Option B — Pointer-Based Injection Strategy (Safe Method)
✔ Goal:

Replace original in-file strings with fixed-length placeholders,
and redirect them to an external strings.tbl file.

✔ Why this works:
- offsets stay unchanged
- script logic stays intact
- only the content of string references changes
- the engine reads text dynamically from the table

##  #️⃣ 4. How the Translation Injection Works
4.1 Create an external string table

Example strings.tbl:

```markdown
STR_0001 = "Summer is finally over…"
STR_0002 = "When did I truly feel that?"
STR_0003 = "Ah, it's already time to leave…"
```


Stored as:

```markdown
{
  "STR_0001": "Summer is finally over…",
  "STR_0002": "When did I truly feel that?",
  "STR_0003": "Ah, it's already time to leave…"
}
```


Your toolkit will create this automatically.

##  #️⃣ 5. Patching the WSC File

Each string reference becomes:

🟦 Original
`夏が終わった――\nそう実感した瞬間はいつだっただろう？%K%P`

🟩 Patched
`<<STR_0001>>%K%P`

The placeholder must NOT exceed the original byte length.

So for long strings:
`<<STR_0001>>`

remains tiny (≤20 bytes).

This ensures:

✔ No offsets shift
✔ No pointer tables break
✔ Safe to inject any translation length

#  #️⃣ 6. Algorithm for the Patching Tool

Here is the exact algorithm your re-injection script must follow:

Step 1 — Load YAML
```python
yaml_data = load_yaml("09_01.yaml")
```

Step 2 — For each entry:
```python
index = generate_string_id()
jp_range = entry['id']
tl = entry['tl'] or entry['jp']

```

Step 3 — Store translation in strings.tbl
```python
table["STR_0001"] = tl
```

Step 4 — Replace the original string in WSC

If original string area is:

```
<start:end> JP_STRING
```

Replace JP_STRING with:
`<<STR_0001>>`

Step 5 — Pad with null bytes if necessary
If placeholder is shorter than original area:

```
pad = (original_length - placeholder_length)
append "\x00" * pad
```

Step 6 — Write modified WSC

Write this to:

`patched/[folder name same as translated yaml]/09_01.wsc`

#  #️⃣ 7. Game Engine Hooking (Reader Layer)

Game engine must be able to read external strings:
Pseudo-code inside engine scripting loader
```
if (token starts with "<<STR_") {
    load external string table
    replace token with mapped translation
}
```


If the engine cannot be modified directly,
you can use:

1. DLL injection
2. Script command hook
3. File redirection
4. Custom command opcode

This repo does not modify the engine directly,
but produces compatible WSC files.


#  #️⃣ 8. Repacking wsc files back to ARC
-Allow claude to plan and think on this end
-create a working directory for this output
