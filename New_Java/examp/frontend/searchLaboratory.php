<?php

require_once('DatabaseHelper.php');


$database = new DatabaseHelper();

// variables from GET
$labor_id = '';
if (isset($_GET['labor_id'])) {
    $labor_id = $_GET['labor_id'];
}


$laboratory_array = $database->searchLaboratory($labor_id);
?>

<html>
<head>
    <title>Laboratory Search Results</title>
</head>
<body>
<h1>Laboratory Search Results</h1>

<!-- Display search results -->
<?php if (count($laboratory_array) > 0) : ?>
    <table border="1">
        <tr>
            <th>Labor ID</th>
            <th>Description</th>
            <th>Capacity</th>
            <th>University ID</th>
        </tr>
        <?php foreach ($laboratory_array as $lab) : ?>
            <tr>
                <td><?php echo htmlspecialchars($lab['LABOR_ID']); ?></td>
                <td><?php echo htmlspecialchars($lab['DESCRIPTION']); ?></td>
                <td><?php echo htmlspecialchars($lab['CAPACITY']); ?></td>
                <td><?php echo htmlspecialchars($lab['UNIV_ID']); ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
<?php else : ?>
    <p>No laboratories found with the specified ID.</p>
<?php endif; ?>

<br>
<a href="index.php">Go back</a>
</body>
</html>
