<?php
require_once('DatabaseHelper.php');
$database = new DatabaseHelper();

$labor_id = '';
if(isset($_POST['labor_id'])){
    $labor_id = $_POST['labor_id'];
}


$success = $database->deleteLaboratory($labor_id);


if ($success){
    echo "Laboratory with ID '{$labor_id}' successfully deleted!";
}
else{
    echo "Error: can't delete Laboratory with ID '{$labor_id}'!";
}

// back to index page
echo "<br><a href='index.php'>Go back</a>";
?>
