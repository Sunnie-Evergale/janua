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
    echo "This is to show that variable name in arguments does not affect passing by reference.:::::::::::::: {$args} <br/>";

}
$hope="Makoto";
improvedIkemen($hope);

function returnFunc($name){
    return $name;
}
$despair=returnFunc("Junko");
echo "This is to show that functions can have return values.:::::::::::::: {$despair}<br/>";


function multipleReturnFunc($name, $name2){
    return array($name,$name2);
}
$ultimate=multipleReturnFunc("Hajime", "Chiaki");
echo "This is to show that functions can have <b>multiple</b> return values.:::::::::::::: {$ultimate[0]}.{$ultimate[1]}<br/>";


echo  "<h1>Notes</h1>";
echo "<ul>
<li>Return can be used a break in loops and switch statements.</li>
<li>Instead of echo, use Return \"Value\"</li>
<li>Return can return a string</li>
<li>Return exits a function immediately.</li>
<li>PHP functions only lets us return one thing</li>
<li>Use array to return more than one values</li>
</ul>"




?>
</body>
</html>