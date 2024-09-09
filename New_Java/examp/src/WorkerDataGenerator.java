<<<<<<< HEAD
import com.github.javafaker.Faker;
import java.sql.*;

public class WorkerDataGenerator {
    private Connection con;
    private Faker faker;

    public WorkerDataGenerator(Connection con) {
        this.con = con;
        this.faker = new Faker();
    }

    public void generateWorkerData() throws SQLException {
        String sql = "INSERT INTO Worker (Worker_ID, Name, Email, Date_of_birth) VALUES (?, ?, ?, ?)";
        try (PreparedStatement pstmt = con.prepareStatement(sql)) {
            con.setAutoCommit(false);

            for (int i = 1; i <= 2000; i++) {
                pstmt.setInt(1, i);
                pstmt.setString(2, faker.name().fullName());
                String email = faker.internet().emailAddress("worker" + i);
                pstmt.setString(3, email);
                pstmt.setDate(4, new java.sql.Date(faker.date().birthday(18, 65).getTime()));//need function getTime via problem with format of data
                pstmt.addBatch();

                if (i % 100 == 0) { // just for efficiency
                    pstmt.executeBatch();
                    con.commit();
                }
            }

            pstmt.executeBatch();
            con.commit();
        } catch (SQLException e) {
            e.printStackTrace();
            con.rollback();
        } finally {
            con.setAutoCommit(true);
        }
    }
}
=======
import com.github.javafaker.Faker;
import java.sql.*;

public class WorkerDataGenerator {
    private Connection con;
    private Faker faker;

    public WorkerDataGenerator(Connection con) {
        this.con = con;
        this.faker = new Faker();
    }

    public void generateWorkerData() throws SQLException {
        String sql = "INSERT INTO Worker (Worker_ID, Name, Email, Date_of_birth) VALUES (?, ?, ?, ?)";
        try (PreparedStatement pstmt = con.prepareStatement(sql)) {
            con.setAutoCommit(false);

            for (int i = 1; i <= 2000; i++) {
                pstmt.setInt(1, i);
                pstmt.setString(2, faker.name().fullName());
                String email = faker.internet().emailAddress("worker" + i);
                pstmt.setString(3, email);
                pstmt.setDate(4, new java.sql.Date(faker.date().birthday(18, 65).getTime()));//need function getTime via problem with format of data
                pstmt.addBatch();

                if (i % 100 == 0) { // just for efficiency
                    pstmt.executeBatch();
                    con.commit();
                }
            }

            pstmt.executeBatch();
            con.commit();
        } catch (SQLException e) {
            e.printStackTrace();
            con.rollback();
        } finally {
            con.setAutoCommit(true);
        }
    }
}
>>>>>>> eead956efcab8f77cd289575815d74a798fdaa14
