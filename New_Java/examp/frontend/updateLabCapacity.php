<?php
require_once('DatabaseHelper.php');
$database = new DatabaseHelper();

$lab_id = isset($_POST['lab_id']) ? $_POST['lab_id'] : '';
$new_capacity = isset($_POST['new_capacity']) ? $_POST['new_capacity'] : '';

// Variables for the output parameters
$old_capacity = 0;
$error_code = 0;


$success = $database->updateLabCapacity($lab_id, $new_capacity, $old_capacity, $error_code);


if ($success && $error_code == 1) {
    echo "Capacity updated successfully! Old Capacity: $old_capacity, New Capacity: $new_capacity";
} else {
    echo "Error: Unable to update capacity. Error Code: $error_code";
}

// back to index page
echo "<br><a href='index.php'>Go back</a>";
?>
