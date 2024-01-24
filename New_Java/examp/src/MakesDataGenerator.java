import java.sql.*;
import java.util.Random;

public class MakesDataGenerator {
    private Connection con;
    private int numOfWorkers;
    private int numOfProjects;
    private int numOfReports;
    private Random random;

    public MakesDataGenerator(Connection con, int numOfWorkers, int numOfProjects, int numOfReports) {
        this.con = con;
        this.numOfWorkers = numOfWorkers;
        this.numOfProjects = numOfProjects;
        this.numOfReports = numOfReports;
        this.random = new Random();
    }

    public void generateData() throws SQLException {
        String sql = "INSERT INTO Makes (Worker_ID, Project_ID, Report_ID) VALUES (?, ?, ?)";
        String checkSql = "SELECT 1 FROM Makes WHERE Worker_ID = ? AND Project_ID = ? AND Report_ID = ?"; // just for duplicates

        try (PreparedStatement pstmt = con.prepareStatement(sql);
             PreparedStatement checkStmt = con.prepareStatement(checkSql)) {
            con.setAutoCommit(false);
            // will be a lot of rows
            for (int i = 1; i <= numOfWorkers; i++) {
                int projectsPerWorker = random.nextInt(5) + 1;
                for (int j = 0; j < projectsPerWorker; j++) {
                    int projectId = random.nextInt(numOfProjects) + 1;
                    int reportsPerProject = random.nextInt(3) + 1;
                    for (int k = 0; k < reportsPerProject; k++) {
                        int reportId = random.nextInt(numOfReports) + 1;

                        // Check if combination already exists
                        checkStmt.setInt(1, i);
                        checkStmt.setInt(2, projectId);
                        checkStmt.setInt(3, reportId);
                        ResultSet rs = checkStmt.executeQuery();
                        if (!rs.next()) { // check for duplicates
                            try {
                                pstmt.setInt(1, i);
                                pstmt.setInt(2, projectId);
                                pstmt.setInt(3, reportId);
                                pstmt.executeUpdate();
                                con.commit();
                            } catch (SQLException e) {
                                System.err.println("Failed to insert row for Worker_ID: " + i + ", Project_ID: " + projectId + ", Report_ID: " + reportId);
                                con.rollback();
                            }
                        }
                    }
                }
            }
        } finally {
            con.setAutoCommit(true);
        }
    }


}
