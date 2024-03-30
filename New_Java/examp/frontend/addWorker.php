<?php
require_once('DatabaseHelper.php');
$database = new DatabaseHelper();

$worker_id = '';
if(isset($_POST['worker_id'])){
    $worker_id = $_POST['worker_id'];
}

$name = '';
if(isset($_POST['name'])){
    $name = $_POST['name'];
}

$email = '';
if(isset($_POST['email'])){
    $email = $_POST['email'];
}

$dob = '';
if(isset($_POST['dob'])){
    $dob = $_POST['dob'];
}


$success = $database->insertWorker($worker_id, $name, $email, $dob);

// Check res
if ($success){
    echo "Worker '{$name}' successfully added!";
}
else{
    echo "Error: can't add Worker '{$name}'!";
}

// back to index page
echo "<br><a href='index.php'>Go back</a>";
?>
