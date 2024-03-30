import com.github.javafaker.Faker;
import java.sql.*;

public class UniversityDataGenerator_2 {
    private Connection con;
    private Faker faker;

    public UniversityDataGenerator_2(Connection con) {
        this.con = con;
        this.faker = new Faker();
    }

    public void generateData() {
        String sql = "INSERT INTO University (University_ID, City, Street) VALUES (?, ?, ?)";

        try (PreparedStatement pstmt = con.prepareStatement(sql)) {
            con.setAutoCommit(false); // Start transaction

            for (int i = 1; i <= 100; i++) {
                pstmt.setInt(1, i);
                pstmt.setString(2, faker.address().city());
                pstmt.setString(3, faker.address().streetName());
                pstmt.addBatch();

                if (i % 100 == 0) {
                    System.out.println("Processed " + i + " records");
                    pstmt.executeBatch();
                    con.commit();
                }
            }

            pstmt.executeBatch();
            con.commit(); //
            System.out.println("All university data inserted successfully");

        } catch (SQLException e) {
            e.printStackTrace();
            try {
                con.rollback();
            } catch (SQLException se) {
                se.printStackTrace();
            }
        } finally {
            try {
                con.setAutoCommit(true);
            } catch (SQLException se) {
                se.printStackTrace();
            }
        }
    }
}
