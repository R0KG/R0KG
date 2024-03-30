<?php
require_once('DatabaseHelper.php');
$database = new DatabaseHelper();

$worker_id = '';
if(isset($_GET['worker_id'])){
    $worker_id = $_GET['worker_id'];
}


$worker_array = $database->searchWorker($worker_id);

// Display results
if (count($worker_array) > 0) {
    echo "<h1>Worker Search Results</h1>";
    echo "<table border='1'>";
    echo "<tr><th>Worker ID</th><th>Name</th><th>Email</th><th>Date of Birth</th></tr>";
    foreach ($worker_array as $worker) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($worker['WORKER_ID']) . "</td>";
        echo "<td>" . htmlspecialchars($worker['NAME']) . "</td>";
        echo "<td>" . htmlspecialchars($worker['EMAIL']) . "</td>";
        echo "<td>" . htmlspecialchars($worker['DATE_OF_BIRTH']) . "</td>";
        echo "</tr>";
    }
}