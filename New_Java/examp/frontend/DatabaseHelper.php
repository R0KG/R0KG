<?php

class DatabaseHelper
{
    const username = 'a11919434';
    const password = 'dbs23';
    const con_string = '//oracle19.cs.univie.ac.at:1521/orclcdb';

    protected $conn;

    public function __construct()
    {
        try {
            $this->conn = oci_connect(
                DatabaseHelper::username,
                DatabaseHelper::password,
                DatabaseHelper::con_string
            );

            if (!$this->conn) {
                die("DB error: Connection can't be established!");
            }

        } catch (Exception $e) {
            die("DB error: {$e->getMessage()}");
        }
    }

    public function __destruct()
    {
        oci_close($this->conn);
    }


    public function selectAllWorkers()
    {
        $sql = "SELECT * FROM Worker";
        $res = array();
        $statement = oci_parse($this->conn, $sql);
        oci_execute($statement);


        oci_fetch_all($statement, $res, 0, 25, OCI_FETCHSTATEMENT_BY_ROW);

        oci_free_statement($statement);
        return $res;
    }

    public function selectAllResearchers()
    {
        $sql = "SELECT * FROM Researcher";
        $res = array();
        $statement = oci_parse($this->conn, $sql);
        oci_execute($statement);
        oci_fetch_all($statement, $res, 0, 25, OCI_FETCHSTATEMENT_BY_ROW);
        oci_free_statement($statement);
        return $res;
    }
    public function selectAllProjects()
    {
        $sql = "SELECT * FROM Project";
        $res = array();
        $statement = oci_parse($this->conn, $sql);
        oci_execute($statement);
        oci_fetch_all($statement, $res, 0, 25, OCI_FETCHSTATEMENT_BY_ROW);
        oci_free_statement($statement);
        return $res;
    }
    public function selectAllLaboratories()
    {
        $sql = "SELECT * FROM Laboratory";
        $res = array();
        $statement = oci_parse($this->conn, $sql);
        oci_execute($statement);
        oci_fetch_all($statement, $res, 0, 25, OCI_FETCHSTATEMENT_BY_ROW);
        oci_free_statement($statement);
        return $res;
    }




    public function insertWorker($worker_id, $name, $email, $dob)
    {
        $sql = "INSERT INTO Worker (Worker_ID, Name, Email, Date_of_birth) VALUES (:worker_id, :name, :email, TO_DATE(:dob, 'YYYY-MM-DD'))";
        $statement = oci_parse($this->conn, $sql);

        // Bind variables
        oci_bind_by_name($statement, ':worker_id', $worker_id);
        oci_bind_by_name($statement, ':name', $name);
        oci_bind_by_name($statement, ':email', $email);
        oci_bind_by_name($statement, ':dob', $dob);

        $success = oci_execute($statement) && oci_commit($this->conn);
        oci_free_statement($statement);
        return $success;
    }





    public function insertLaboratory($labor_id, $description, $capacity, $univ_id)
    {
        $sql = "INSERT INTO Laboratory (Labor_ID, Description, Capacity, Univ_ID) VALUES (:labor_id, :description, :capacity, :univ_id)";
        $statement = oci_parse($this->conn, $sql);

        // Bind variables
        oci_bind_by_name($statement, ':labor_id', $labor_id);
        oci_bind_by_name($statement, ':description', $description);
        oci_bind_by_name($statement, ':capacity', $capacity);
        oci_bind_by_name($statement, ':univ_id', $univ_id);

        $success = oci_execute($statement) && oci_commit($this->conn);
        oci_free_statement($statement);
        return $success;
    }
    public function deleteLaboratory($labor_id)
    {

        $sql = "DELETE FROM Laboratory WHERE LABOR_ID = :labor_id";


        $statement = oci_parse($this->conn, $sql);


        oci_bind_by_name($statement, ':labor_id', $labor_id);


        $success = oci_execute($statement) && oci_commit($this->conn);


        oci_free_statement($statement);


        return $success;
    }
    public function searchLaboratory($labor_id)
    {

        $sql = "SELECT * FROM Laboratory WHERE LABOR_ID = :labor_id";


        $statement = oci_parse($this->conn, $sql);


        oci_bind_by_name($statement, ':labor_id', $labor_id);


        oci_execute($statement);


        $res = array();
        oci_fetch_all($statement, $res, 0, -1, OCI_FETCHSTATEMENT_BY_ROW);


        oci_free_statement($statement);


        return $res;
    }

    public function searchWorker($worker_id)
    {

        $sql = "SELECT * FROM Worker WHERE WORKER_ID = :worker_id";


        $statement = oci_parse($this->conn, $sql);


        oci_bind_by_name($statement, ':worker_id', $worker_id);


        oci_execute($statement);


        $res = array();
        oci_fetch_all($statement, $res, 0, -1, OCI_FETCHSTATEMENT_BY_ROW);


        oci_free_statement($statement);


        return $res;
    }

    public function deleteWorker($worker_id)
    {

        $sql = "DELETE FROM Laboratory WHERE LABOR_ID = :worker_id";


        $statement = oci_parse($this->conn, $sql);


        oci_bind_by_name($statement, ':worker_id', $worker_id);


        $success = oci_execute($statement) && oci_commit($this->conn);


        oci_free_statement($statement);


        return $success;
    }
    public function updateLabCapacity($lab_id, $new_capacity, &$old_capacity, &$error_code) {
        $sql = 'BEGIN UPDATE_LAB_CAPACITY(:lab_id, :new_capacity, :old_capacity, :error_code); END;';
        $statement = oci_parse($this->conn, $sql);


        oci_bind_by_name($statement, ':lab_id', $lab_id);
        oci_bind_by_name($statement, ':new_capacity', $new_capacity);
        oci_bind_by_name($statement, ':old_capacity', $old_capacity, 32); // 32 is the size of the variable
        oci_bind_by_name($statement, ':error_code', $error_code, 32);


        $success = oci_execute($statement);


        oci_free_statement($statement);

        return $success;
    }

}
