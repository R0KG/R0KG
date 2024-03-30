<?php
//include DatabaseHelper.php file
require_once('DatabaseHelper.php');

//instantiate DatabaseHelper class
$database = new DatabaseHelper();

//Grab variable id from POST request
$person_id = '';
if(isset($_POST['id'])){
    $person_id = $_POST['id'];
}

// Delete method
$error_code = $database->deletePerson( $person_id);

// Check result
if ($error_code == 1){
    echo "Person with ID: '{$person_id}' successfully deleted!'";
}
else{
    echo "Error can't delete Person with ID: '{$person_id}'. Errorcode: {$error_code}";
}
?>

<!-- link back to index page-->
<br>
<a href="index.php">
    go back
</a>