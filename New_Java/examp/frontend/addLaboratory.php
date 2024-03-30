<?php
require_once('DatabaseHelper.php');
$database = new DatabaseHelper();

//variables from POST
$labor_id = '';
if (isset($_POST['labor_id'])) {
    $labor_id = $_POST['labor_id'];
}

$description = '';
if (isset($_POST['description'])) {
    $description = $_POST['description'];
}

$capacity = '';
if (isset($_POST['capacity'])) {
    $capacity = $_POST['capacity'];
}

$univ_id = '';
if (isset($_POST['univ_id'])) {
    $univ_id = $_POST['univ_id'];
}


$success = $database->insertLaboratory($labor_id, $description, $capacity, $univ_id);

// Check res
if ($success) {
    echo "Laboratory '{$description}' successfully added!";
} else {
    echo "Error: can't insert Laboratory '{$description}'!";
}

echo "<br><a href='index.php'>Go back</a>";
?>
