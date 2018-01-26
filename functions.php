<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Functions</title>
</head>
<body>
<?php
function improvedIkemen($args){
    echo "Variable name in arguments does not affect passing by reference.:::::::::::::: {$args} <br/>";

}
$hope="Makoto";
improvedIkemen($hope);

function returnFunc($name){
    return $name;
}
$despair=returnFunc("Junko");
echo "Functions can have return values.:::::::::::::: {$despair}<br/>";


function multipleReturnFunc($name, $name2){
    return array($name,$name2);
}
$ultimate=multipleReturnFunc("Hajime", "Chiaki");
echo "Functions can have <b>multiple</b> return values.:::::::::::::: {$ultimate[0]}.{$ultimate[1]}<br/>";
list($ordinary,$hacker)=multipleReturnFunc("Hajime", "Chiaki");
echo "Good programming practice is using List instead of array.:::::::::::::: {$ordinary}.{$hacker}<br/>";
$listCode=htmlspecialchars("list($ordinary,$hacker)=multipleReturnFunc(\"Hajime\", \"Chiaki\");");

echo "<blockquote>{$listCode}</blockquote>";


echo  "<h1>Notes</h1>";
echo "<ul>
<li>Return can be used a break in loops and switch statements.</li>
<li>Instead of echo, use Return \"Value\"</li>
<li>Return can return a string</li>
<li>Return exits a function immediately.</li>
<li>PHP functions only lets us return one thing.</li>
<li>Use array to return more than one values. return array(value1,value2);</li>
</ul>";

echo  "<h1>Useful functions</h1>";
echo "<ul>
<li>isset() checks if variable has value</li>
<li>list(value1,value2) breaks down array to named variables instead of array[0]</li>
<li>htmlspecialchars() converts code to literal code. Note that you need \ to escape quotation marks.</li>
<li>ucwords() upper case words</li>
</ul>";



?>
</body>
</html>