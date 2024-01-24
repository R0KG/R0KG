
<?php

require_once('DatabaseHelper.php');


$database = new DatabaseHelper();


$worker_array = $database->selectAllWorkers();
$researcher_array = $database->selectAllResearchers();
$project_array = $database->selectAllProjects();
$laboratory_array = $database->selectAllLaboratories();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Database Interface</title>

    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .container {
            padding-top: 20px;
        }
        h1, h2 {
            margin-top: 20px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1 class="text-center">Database Interface</h1>

    <!-- Worker Data Section -->
    <h2>Worker Data</h2>
    <table class="table table-bordered table-striped">

        <tr>
            <th>Worker ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Date of Birth</th>
        </tr>

        <?php foreach ($worker_array as $worker): ?>
            <tr>
                <td><?php echo htmlspecialchars($worker['WORKER_ID']); ?></td>
                <td><?php echo htmlspecialchars($worker['NAME']); ?></td>
                <td><?php echo htmlspecialchars($worker['EMAIL']); ?></td>
                <td><?php echo htmlspecialchars($worker['DATE_OF_BIRTH']); ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
    <hr>

    <!-- Worker Functions -->
    <h2>Add New Worker:</h2>
    <form method="post" action="addWorker.php">

        <div>
            <label for="worker_id">Worker ID:</label>
            <input id="worker_id" name="worker_id" type="number" min="1">
        </div>
        <br>


        <div>
            <label for="name">Name:</label>
            <input id="name" name="name" type="text" maxlength="255">
        </div>
        <br>


        <div>
            <label for="email">Email:</label>
            <input id="email" name="email" type="email">
        </div>
        <br>


        <div>
            <label for="dob">Date of Birth:</label>
            <input id="dob" name="dob" type="date">
        </div>
        <br>


        <div>
            <button type="submit">
                Add Worker
            </button>
        </div>
    </form>
    <br>
    <hr>


    <!-- Delete Worker -->
    <h2>Delete Worker: </h2>
    <form method="post" action="deleteWorker.php">

        <div>
            <label for="del_worker_id">Worker ID:</label>
            <input id="del_worker_id" name="worker_id" type="number" min="1">
        </div>
        <br>


        <div>
            <button type="submit">
                Delete Worker
            </button>
        </div>
    </form>
    <br>
    <hr>

    <!-- Search Worker form -->
    <h2>Worker Search:</h2>
    <form method="get" action="searchWorker.php">

        <div>
            <label for="worker_id">Worker ID:</label>
            <input id="worker_id" name="worker_id" type="number" min="1">
        </div>
        <br>


        <div>
            <button id='submit' type='submit'>
                Search
            </button>
        </div>
    </form>
    <br>
    <hr>




    <!-- Researcher Data -->
    <h2>Researcher Data:</h2>
    <table border="1">
        <tr>
            <th>Researcher ID</th>
            <th>Research Area</th>
            <th>Character</th>

        </tr>
        <?php foreach ($researcher_array as $researcher) : ?>
            <tr>
                <td><?php echo $researcher['RESEARCHER_ID']; ?></td>
                <td><?php echo $researcher['RESEARCH_AREA']; ?></td>
                <td><?php echo $researcher['CHARACTER']; ?></td>
            </tr>
        <?php endforeach; ?>
    </table>

    <hr>

    <!-- Project Data -->
    <h2>Project Data:</h2>
    <table border="1">
        <tr>
            <th>Project ID</th>
            <th>Direction of Research</th>
            <th>Project Name</th>

        </tr>
        <?php foreach ($project_array as $project) : ?>
            <tr>
                <td><?php echo $project['PROJECT_ID']; ?></td>
                <td><?php echo $project['DIRECTION_OF_RESEARCH']; ?></td>
                <td><?php echo $project['PROJECT_NAME']; ?></td>

            </tr>
        <?php endforeach; ?>
    </table>

    <hr>

    <!-- Laboratory Data -->
    <h2>Laboratory Data:</h2>
    <table border="1">
        <tr>
            <th>Labor ID</th>
            <th>Description</th>
            <th>Capacity</th>
            <th>University ID</th>
        </tr>
        <?php foreach ($laboratory_array as $lab) : ?>
            <tr>
                <td><?php echo $lab['LABOR_ID']; ?></td>
                <td><?php echo $lab['DESCRIPTION']; ?></td>
                <td><?php echo $lab['CAPACITY']; ?></td>
                <td><?php echo $lab['UNIV_ID']; ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
    <hr>

    <h2>Add New Laboratory:</h2>
    <form method="post" action="addLaboratory.php">

        <div>
            <label for="labor_id">Laboratory ID:</label>
            <input id="labor_id" name="labor_id" type="number" min="1">
        </div>
        <br>


        <div>
            <label for="description">Description:</label>
            <input id="description" name="description" type="text" maxlength="255">
        </div>
        <br>


        <div>
            <label for="capacity">Capacity:</label>
            <input id="capacity" name="capacity" type="number" min="1">
        </div>
        <br>


        <div>
            <label for="univ_id">University ID:</label>
            <input id="univ_id" name="univ_id" type="number" min="1">
        </div>
        <br>


        <div>
            <button type="submit">
                Add Laboratory
            </button>
        </div>
    </form>
    <br>
    <hr>
    <!-- Delete Laboratory -->
    <h2>Delete Laboratory: </h2>
    <form method="post" action="deleteLaboratory.php">

        <div>
            <label for="del_labor_id">Labor ID:</label>
            <input id="del_labor_id" name="labor_id" type="number" min="1">
        </div>
        <br>


        <div>
            <button type="submit">
                Delete Laboratory
            </button>
        </div>
    </form>
    <br>
    <hr>


    <!-- Search Laboratory form -->
    <h2>Laboratory Search:</h2>
    <form method="get" action="searchLaboratory.php">

        <div>
            <label for="labor_id">Labor ID:</label>
            <input id="labor_id" name="labor_id" type="number"  min="1">
        </div>
        <br>


        <div>
            <button id='submit' type='submit'>
                Search
            </button>
        </div>
    </form>
    <br>
    <hr>

    <h2>Update Laboratory Capacity:</h2>
    <form method="post" action="updateLabCapacity.php">
        <div>
            <label for="lab_id">Laboratory ID:</label>
            <input id="lab_id" name="lab_id" type="number" min="1" required>
        </div>
        <br>

        <div>
            <label for="new_capacity">New Capacity:</label>
            <input id="new_capacity" name="new_capacity" type="number" min="1" required>
        </div>
        <br>

        <button type="submit">Update Capacity</button>
    </form>
    <hr>



    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
</div>
</body>
</html>















