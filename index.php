<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Stormy.Local</title>

<?php
/**
 * Created by PhpStorm.
 * User: Sunnie
 * Date: 1/20/2018
 * Time: 10:30 AM
 */

/** If Statement*/
echo "<h1>Tips:</h1>";
echo "PHP storm HTML5: ! then Tab <br/>";

echo "<h1>Variable logic</h1>";

$a=10;
$b=20;
$result=0;

echo "<h1>if{} else{} elseif{}</h1>";
if ($a>$b){
    echo "A is larger than <BR/>";
}
else{
    echo "B is huge.<BR/>";
}

$result=$a+$b;
echo "Result $result<BR/>";
echo "Result A: {$a}<BR/>";
echo "<h1>forloop();</h1>";

for ($a=0;$a<=2;$a++){
    echo "Result A [$a]: {$a}<BR/>";

}

echo "<h1>Array</h1>";
$bishounen =array("hollow" => "feelings",
    "teleportation" => "escape",
    "mindless" => "drone");


echo "<h1>foreach(){</h1>";
foreach ($bishounen as $otoko => $kimochi){
    $labelNew = ucwords($otoko);
    echo "{$labelNew} ".ucwords($kimochi)."<br/>";
}

echo "<br/>";
//Functions
echo "<h1>Functions</h1>";

function SAY_HELLO(){
    echo "Say hello";
}
function SAY_HELLO_TO($word){
    echo "Hi {$word}!";
}

echo "Simple function";
SAY_HELLO();
echo "<br/>";
echo "Intermediate function";
SAY_HELLO_TO("Sunnie");
echo "<br/><br/><br/>";
echo "Note:You cannot use the same function name even with args <br/>";
echo "Note: There is no space after function call </br/>";
echo "Note: PHP 4-5 finds functions first so you can define function after. Highly not recommended. </br/>";
echo "Functions are not case insensitive. Variables are case sensitive. </br/>";

?>

</head>
<body>

</body>
</html>

