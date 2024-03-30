import java.sql.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;
import com.github.javafaker.Faker;

public class CommunicatesDataGenerator {
    private Connection con;
    private Random random;
    private List<String> communicationTypes;
    private Faker faker;

    public CommunicatesDataGenerator(Connection con) {
        this.con = con;
        this.random = new Random();
        this.faker = new Faker();
        this.communicationTypes = Arrays.asList("Email", "Phone", "Meeting", "Video Call", "Chat");
    }

    private String getRandomCommunicationType() {
        return communicationTypes.get(random.nextInt(communicationTypes.size()));
    }

    private Timestamp getRandomCommunicationTime() {

        java.util.Date date = faker.date().between(new java.util.Date(119, 0, 1), new java.util.Date(123, 11, 31));
        return new Timestamp(date.getTime());
    }

    public void generateData() throws SQLException {
        String sql = "INSERT INTO Communicates (Sender_ID, Receiver_ID, Communication_Type, Communication_Time) VALUES (?, ?, ?, ?)";

        // SQL to find pairs of researchers in the same laboratory
        String findPairsSql =
                "SELECT e1.Worker_ID AS Researcher_ID1, e2.Worker_ID AS Researcher_ID2 " +
                        "FROM Employs e1 " +
                        "JOIN Researcher r1 ON e1.Worker_ID = r1.Researcher_ID " + // select only researchers
                        "JOIN Employs e2 ON e1.Labor_ID = e2.Labor_ID " + // same labor as e1
                        "JOIN Researcher r2 ON e2.Worker_ID = r2.Researcher_ID " + //select only researchers
                        "WHERE e1.Worker_ID != e2.Worker_ID"; // not the same person

        try (PreparedStatement pstmt = con.prepareStatement(sql);
             Statement findPairsStmt = con.createStatement()) {
            con.setAutoCommit(false);

            ResultSet rs = findPairsStmt.executeQuery(findPairsSql);
            Set<String> addedPairs = new HashSet<>(); // To prevent duplicate entries

            while (rs.next()) {
                int researcherId1 = rs.getInt("Researcher_ID1");
                int researcherId2 = rs.getInt("Researcher_ID2");
                String pairKey = researcherId1 + "-" + researcherId2;

                if (!addedPairs.contains(pairKey)) {
                    pstmt.setInt(1, researcherId1);
                    pstmt.setInt(2, researcherId2);
                    pstmt.setString(3, getRandomCommunicationType());
                    pstmt.setTimestamp(4, getRandomCommunicationTime());
                    pstmt.addBatch();
                    addedPairs.add(pairKey); // Mark this pair as added
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
