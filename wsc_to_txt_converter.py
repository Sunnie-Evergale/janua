#!/usr/bin/env python3
"""
wsc_to_txt_converter.py

Simple converter to extract printable text segments from a .wsc file and
emit a plain .txt in the same *style* as the example you provided.

This is a best-effort, format-preserving converter:
- It scans the binary for contiguous non-null byte runs,
  tries to decode each run as Shift_JIS (falling back to UTF-8),
  and keeps runs that look like human-readable text.
- It writes lines of the form:
    L{index}: <{start:08X}:{end:08X}> {decoded_text} %K%P
  which mirrors the example layout (offset ranges and text).

Notes / limitations:
- This tool aims to reproduce the textual layout/format, not to perfectly
  re-create any domain-specific markers embedded in the .wsc format.
- If you need an exact 1:1 reproduction of the upstream converter's
  output (including speaker tags, custom markers, or precise offsets
  from pointer tables), we can iterate — but this script is a
  general-purpose starting point.

Usage:
    python3 wsc_to_txt_converter.py /path/to/09_04.wsc > 09_04.txt

"""

import sys
import re
from typing import List, Tuple

MIN_RUN_BYTES = 8  # minimum contiguous bytes to consider

PRINTABLE_RE = re.compile(r"[\u3000-\u30FF\u4E00-\u9FFF\u3040-\u309F\uFF00-\uFFEF\u0020-\u007E]+")

def is_mostly_printable(s: str) -> bool:
    if not s:
        return False
    matches = PRINTABLE_RE.findall(s)
    printable = sum(len(m) for m in matches)
    return printable >= max(6, len(s) * 0.6)


def find_nonnull_runs(data: bytes) -> List[Tuple[int,int,bytes]]:
    """Return list of (start, end, bytes) for runs without NUL bytes of length>=MIN_RUN_BYTES."""
    runs = []
    start = None
    for i, b in enumerate(data):
        if b != 0:
            if start is None:
                start = i
        else:
            if start is not None:
                if i - start >= MIN_RUN_BYTES:
                    runs.append((start, i, data[start:i]))
                start = None
    # tail
    if start is not None and len(data) - start >= MIN_RUN_BYTES:
        runs.append((start, len(data), data[start:]))
    return runs


def decode_best(bs: bytes) -> str:
    """Try decoding bs with shift_jis then utf-8; return decoded str (strip trailing NULs)."""
    for enc in ("shift_jis", "utf-8", "latin-1"):
        try:
            s = bs.decode(enc)
            # normalize spaces and remove weird control chars except \n and \t
            s = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]+", "", s)
            return s
        except Exception:
            continue
    # fallback latin-1 to preserve bytes as-is
    return bs.decode("latin-1", errors="replace")


def chunk_and_filter_runs(runs: List[Tuple[int,int,bytes]]) -> List[Tuple[int,int,str]]:
    out = []
    for start, end, bs in runs:
        # further split on long sequences of bytes that look like pointers or binary garbage
        # split on sequences of >=4 bytes that are 0x00..0x1F or 0x80..0xFF frequently
        # We'll try simple approach: slide window and extract subruns that decode well.
        s = decode_best(bs)
        # if decoded contains a lot of replacement characters or control junk, try heuristics
        if is_mostly_printable(s):
            out.append((start, end, s.strip()))
            continue
        # otherwise attempt to split by common separators (0x0A, 0x0D, 0x20) in the raw bytes
        # to find smaller readable pieces
        for m in re.finditer(rb"[\x0A\x0D\x20]{1,}", bs):
            pass
        # fallback: try to decode subwindows of bs
        win = 0
        i = 0
        while i < len(bs):
            # expand window until decode looks plausible
            for j in range(i + MIN_RUN_BYTES, min(len(bs), i + 4096) + 1):
                sub = bs[i:j]
                ssub = decode_best(sub)
                if is_mostly_printable(ssub):
                    out.append((start + i, start + j, ssub.strip()))
                    i = j
                    break
            else:
                i += MIN_RUN_BYTES
    # coalesce adjacent or overlapping lines with same text (avoid duplicates)
    coalesced = []
    for st, ed, txt in out:
        if not txt:
            continue
        if coalesced and st <= coalesced[-1][1] + 4:
            # merge
            prev_st, prev_ed, prev_txt = coalesced[-1]
            coalesced[-1] = (prev_st, max(prev_ed, ed), (prev_txt + " " + txt).strip())
        else:
            coalesced.append((st, ed, txt))
    return coalesced


def emit_txt(entries: List[Tuple[int,int,str]], out_file=None):
    if out_file is None:
        out = sys.stdout
    else:
        out = open(out_file, "w", encoding="utf-8")
    for idx, (st, ed, txt) in enumerate(entries):
        # produce lines similar to the example: L{n}: <{hexst}:{hexed}> {txt}%K%P
        line_prefix = f"L{idx}: <{st:08X}:{ed:08X}>"
        # normalize internal newlines to \n and keep them
        txt_norm = txt.replace("\r\n", "\n").replace("\r", "\n")
        # if multi-line, split and emit joined with space, preserving Japanese quotes
        txt_out = txt_norm.replace("\n", "\\n")
        out.write(f"{line_prefix} {txt_out} %K%P\n")
    if out_file is not None:
        out.close()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 wsc_to_txt_converter.py /path/to/file.wsc [out.txt]")
        sys.exit(1)
    path = sys.argv[1]
    out_path = None
    if len(sys.argv) >= 3:
        out_path = sys.argv[2]
    with open(path, "rb") as f:
        data = f.read()
    runs = find_nonnull_runs(data)
    entries = chunk_and_filter_runs(runs)
    # sort by start offset
    entries.sort(key=lambda x: x[0])
    emit_txt(entries, out_path)


if __name__ == "__main__":
    main()
