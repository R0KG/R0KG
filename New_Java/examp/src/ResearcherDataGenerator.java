import com.github.javafaker.Faker;
import java.sql.*;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class ResearcherDataGenerator {
    private Connection con;
    private Faker faker;
    private List<String> researchAreas;
    private List<String> characterTraits;
    public ResearcherDataGenerator(Connection con) {
        this.con = con;
        this.faker = new Faker();
        this.researchAreas = Arrays.asList("Biology", "Physics", "Chemistry", "Computer Science",
                "Mathematics", "Medicine", "Environmental Science",
                "Engineering", "Astronomy", "Robotics");
        this.characterTraits = Arrays.asList(
                "Adventurous", "Affable", "Capable", "Charming", "Compassionate",
                "Confident", "Conscientious", "Courageous", "Diligent", "Empathetic",
                "Generous", "Honest", "Innovative", "Intelligent", "Meticulous",
                "Optimistic", "Perceptive", "Resilient", "Resourceful", "Sincere",
                "Thoughtful", "Versatile", "Witty"
        );
    }


    public void generateData() throws SQLException {
        String sql = "INSERT INTO Researcher (Researcher_ID, research_area, Character) VALUES (?, ?, ?)";
        PreparedStatement pstmt = con.prepareStatement(sql);
        Random random = new Random();
        // Starting from 501 Worker_ID = researcher
        for (int i = 501; i <= 2000; i++) {
            String researchArea = researchAreas.get(random.nextInt(researchAreas.size()));
            String character = characterTraits.get(random.nextInt(characterTraits.size()));

            pstmt.setInt(1, i);
            pstmt.setString(2, researchArea);
            pstmt.setString(3, character);
            pstmt.executeUpdate();
        }

        pstmt.close();
    }
}
