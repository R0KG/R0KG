import java.sql.*;
import java.util.HashSet;
import java.util.Set;

public class LeadsDataGenerator {
    private Connection con;

    public LeadsDataGenerator(Connection con) {
        this.con = con;
    }

    public void generateData() throws SQLException {
        String sql = "INSERT INTO Leads (Chief_ID, Researcher_ID) VALUES (?, ?)";

        // SQL to find researchers and head researchers in the same laboratory
        String findPairsSql = "SELECT e1.Worker_ID AS Chief_ID, e2.Worker_ID AS Researcher_ID " +
                "FROM Employs e1 " +
                "JOIN Head_Researcher h ON e1.Worker_ID = h.Chief_ID " + // find headResearchers
                "JOIN Employs e2 ON e1.Labor_ID = e2.Labor_ID " + // same labor
                "JOIN Researcher r ON e2.Worker_ID = r.Researcher_ID " + // find researchers
                "WHERE e1.Worker_ID != e2.Worker_ID"; // not the same man

        try (PreparedStatement pstmt = con.prepareStatement(sql);
             Statement findPairsStmt = con.createStatement()) {
            con.setAutoCommit(false);

            ResultSet rs = findPairsStmt.executeQuery(findPairsSql);
            Set<String> addedPairs = new HashSet<>(); // To prevent duplicate entries

            while (rs.next()) {
                int chiefId = rs.getInt("Chief_ID");
                int researcherId = rs.getInt("Researcher_ID");
                String pairKey = chiefId + "-" + researcherId;

                if (!addedPairs.contains(pairKey)) {
                    pstmt.setInt(1, chiefId);
                    pstmt.setInt(2, researcherId);
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
