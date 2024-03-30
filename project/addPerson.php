<?php
//include DatabaseHelper.php file
require_once('DatabaseHelper.php');

//instantiate DatabaseHelper class
$database = new DatabaseHelper();

//Grab variables from POST request
$name = '';
if(isset($_POST['name'])){
    $name = $_POST['name'];
}

$surname = '';
if(isset($_POST['surname'])){
    $surname = $_POST['surname'];
}

// Insert method
$success = $database->insertIntoPerson($name, $surname);

// Check result
if ($success){
    echo "Person '{$name} {$surname}' successfully added!'";
}
else{
    echo "Error can't insert Person '{$name} {$surname}'!";
}
?>

<!-- link back to index page-->
<br>
<a href="index.php">
    go back
</a>