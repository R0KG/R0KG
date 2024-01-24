import com.github.javafaker.Faker;
import java.sql.*;

public class HeadResearcherDataGenerator {
    private Connection con;
    private Faker faker;

    public HeadResearcherDataGenerator(Connection con) {
        this.con = con;
        this.faker = new Faker();
    }

    public void generateData() throws SQLException {
        String sql = "INSERT INTO Head_Researcher (Chief_ID, Experience, Awards) VALUES (?, ?, ?)";
        PreparedStatement pstmt = con.prepareStatement(sql);

        // first 500 IDs for Head Researchers
        for (int i = 1; i <= 500; i++) {
            int experience = faker.number().numberBetween(1, 40);
            String awards = faker.lorem().sentence(); // just text

            pstmt.setInt(1, i); // Chief_ID = Worker_ID
            pstmt.setInt(2, experience);
            pstmt.setString(3, awards);
            pstmt.executeUpdate();
        }

        pstmt.close();
    }
}
