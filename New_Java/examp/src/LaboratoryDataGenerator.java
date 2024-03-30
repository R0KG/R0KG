import com.github.javafaker.Faker;
import java.sql.*;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class LaboratoryDataGenerator {
    private Connection con;
    private Faker faker;
    private List<String> labTypes;

    public LaboratoryDataGenerator(Connection con) {
        this.con = con;
        this.faker = new Faker();
        this.labTypes = Arrays.asList("Computer Science", "Chemistry", "Physics", "Biology", "Engineering", "Mathematics", "Medicine", "Environmental Science", "Robotics", "Astronomy");
    }


    public void generateData() throws SQLException {
        String sql = "INSERT INTO Laboratory (Labor_ID, Description, Capacity, Univ_ID) VALUES (?, ?, ?, ?)";
        PreparedStatement pstmt = con.prepareStatement(sql);
        Random random = new Random();

        for (int i = 1; i <= 500; i++) {
            int univId = faker.number().numberBetween(1, 101);

            String labType = labTypes.get(random.nextInt(labTypes.size()));
            String description = labType + " Laboratory - " + faker.lorem().sentence();

            pstmt.setInt(1, i);
            pstmt.setString(2, description);
            pstmt.setInt(3, faker.number().numberBetween(1, 101));
            pstmt.setInt(4, univId);
            pstmt.executeUpdate();
        }

        pstmt.close();
    }
}
