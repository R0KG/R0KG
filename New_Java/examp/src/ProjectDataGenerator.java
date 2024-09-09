<<<<<<< HEAD
import com.github.javafaker.Faker;
import java.sql.*;

public class ProjectDataGenerator {
    private Connection con;
    private Faker faker;

    public ProjectDataGenerator(Connection con) {
        this.con = con;
        this.faker = new Faker();
    }

    public void generateData(int numberOfProjects) throws SQLException {
        String sql = "INSERT INTO Project (Project_ID, direction_of_research, Project_Name) VALUES (?, ?, ?)";
        try (PreparedStatement pstmt = con.prepareStatement(sql)) {
            con.setAutoCommit(false);

            for (int i = 1; i <= numberOfProjects; i++) {

                String reportName = "Report: " + i;

                pstmt.setInt(1, i);
                pstmt.setString(2, faker.educator().course());
                pstmt.setString(3, reportName);
                pstmt.addBatch();

                if (i % 100 == 0 || i == numberOfProjects) {
                    pstmt.executeBatch();
                    con.commit(); //
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
            if (con != null) {
                con.rollback();
            }
        } finally {
            if (con != null) {
                con.setAutoCommit(true);
            }
        }
    }
}
=======
import com.github.javafaker.Faker;
import java.sql.*;

public class ProjectDataGenerator {
    private Connection con;
    private Faker faker;

    public ProjectDataGenerator(Connection con) {
        this.con = con;
        this.faker = new Faker();
    }

    public void generateData(int numberOfProjects) throws SQLException {
        String sql = "INSERT INTO Project (Project_ID, direction_of_research, Project_Name) VALUES (?, ?, ?)";
        try (PreparedStatement pstmt = con.prepareStatement(sql)) {
            con.setAutoCommit(false);

            for (int i = 1; i <= numberOfProjects; i++) {

                String reportName = "Report: " + i;

                pstmt.setInt(1, i);
                pstmt.setString(2, faker.educator().course());
                pstmt.setString(3, reportName);
                pstmt.addBatch();

                if (i % 100 == 0 || i == numberOfProjects) {
                    pstmt.executeBatch();
                    con.commit(); //
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
            if (con != null) {
                con.rollback();
            }
        } finally {
            if (con != null) {
                con.setAutoCommit(true);
            }
        }
    }
}
>>>>>>> eead956efcab8f77cd289575815d74a798fdaa14
