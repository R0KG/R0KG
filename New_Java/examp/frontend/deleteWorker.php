<?php
require_once('DatabaseHelper.php');
$database = new DatabaseHelper();

$worker_id = '';
if(isset($_POST['worker_id'])){
    $worker_id = $_POST['worker_id'];
}


$success = $database->deleteWorker($worker_id);

// Check res
if ($success){
    echo "Worker with ID '{$worker_id}' successfully deleted!";
}
else{
    echo "Error: can't delete Worker with ID '{$worker_id}'!";
}

// back to index page
echo "<br><a href='index.php'>Go back</a>";
?>
