import java.sql.*;
import java.util.*;
import com.github.javafaker.Faker;
public class EmploysDataGenerator {
    private Connection con;
    private Random random;
    private Faker faker;
    private Map<Integer, Integer> laboratoryCapacityMap; // Map Labor_ID to its capacity
    private Set<Integer> usedLaboratories; // Keep track of laboratories already assigned a Head Researcher

    public EmploysDataGenerator(Connection con) {
        this.con = con;
        this.random = new Random();
        this.faker = new Faker();
        this.laboratoryCapacityMap = new HashMap<>();
        this.usedLaboratories = new HashSet<>();
    }

    public void generateData() throws SQLException {
        loadLaboratoryCapacities();
        String sql = "INSERT INTO Employs (Labor_ID, Worker_ID, Starting_date) VALUES (?, ?, ?)";
        try (PreparedStatement pstmt = con.prepareStatement(sql)) {
            con.setAutoCommit(false);
            assignHeadResearchers(pstmt);
            assignResearchers(pstmt);
            reassignWorkersToDifferentLaboratories();
            con.commit();
        } catch (SQLException e) {
            e.printStackTrace();
            con.rollback();
        } finally {
            con.setAutoCommit(true);
        }
    }
    private void reassignWorkersToDifferentLaboratories() throws SQLException {
        String sql = "INSERT INTO Employs (Labor_ID, Worker_ID, Starting_date) VALUES (?, ?, ?)";

        // Query to find all workers  who are not head researchers
        String workerQuery = "SELECT Worker_ID, Labor_ID FROM Employs WHERE Worker_ID NOT IN (SELECT Chief_ID FROM Head_Researcher)";

        // Query to find all laboratories within the same university
        String labQuery = "SELECT Labor_ID FROM Laboratory WHERE Univ_ID = (SELECT Univ_ID FROM Laboratory WHERE Labor_ID = ?)";

        try (PreparedStatement pstmt = con.prepareStatement(sql);
             Statement workerStmt = con.createStatement();
             PreparedStatement labStmt = con.prepareStatement(labQuery);
             ResultSet workerRs = workerStmt.executeQuery(workerQuery)) {
            while (workerRs.next()) {
                int workerId = workerRs.getInt("Worker_ID");
                int currentLaborId = workerRs.getInt("Labor_ID");

                // Set the parameter for the laboratory query
                labStmt.setInt(1, currentLaborId);

                // Execute the laboratory query
                try (ResultSet labRs = labStmt.executeQuery()) {
                    List<Integer> availableLabs = new ArrayList<>();
                    while (labRs.next()) {
                        int laborId = labRs.getInt("Labor_ID");
                        if (laborId != currentLaborId && laboratoryCapacityMap.getOrDefault(laborId, 0) > 0) {
                            availableLabs.add(laborId);
                        }
                    }

                    // Randomly assign the worker to one of the available labs
                    if (!availableLabs.isEmpty()) {
                        int newLaborId = availableLabs.get(random.nextInt(availableLabs.size()));
                        pstmt.setInt(1, newLaborId);
                        pstmt.setInt(2, workerId);
                        pstmt.setDate(3, getRandomStartDate());
                        pstmt.addBatch();

                        // Update the capacity map
                        int newCapacity = laboratoryCapacityMap.get(newLaborId) - 1;
                        laboratoryCapacityMap.put(newLaborId, newCapacity);
                    }
                }
            }
            pstmt.executeBatch();
        }
    }

    private void loadLaboratoryCapacities() throws SQLException {
        String sql = "SELECT Labor_ID, Capacity FROM Laboratory";
        try (Statement stmt = con.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                int laborId = rs.getInt("Labor_ID");
                int capacity = rs.getInt("Capacity");
                laboratoryCapacityMap.put(laborId, capacity);
            }
        }
    }
    private void assignHeadResearchers(PreparedStatement pstmt) throws SQLException {
        String headResearcherSQL = "SELECT Chief_ID FROM Head_Researcher";
        try (Statement headStmt = con.createStatement(); ResultSet headRs = headStmt.executeQuery(headResearcherSQL)) {
            while (headRs.next()) {
                int headResearcherId = headRs.getInt("Chief_ID");
                int laborId = getNextAvailableLaboratory(); // Get an available laboratory
                if (laborId != -1) {
                    pstmt.setInt(1, laborId);
                    pstmt.setInt(2, headResearcherId);
                    pstmt.setDate(3, getRandomStartDate());
                    pstmt.addBatch();
                    usedLaboratories.add(laborId); // Mark this laboratory as used
                }
            }
            pstmt.executeBatch();
        }
    }

    private int getNextAvailableLaboratory() {
        for (Integer labId : laboratoryCapacityMap.keySet()) {
            if (!usedLaboratories.contains(labId)) {
                return labId;
            }
        }
        return -1; // Return -1 if no available laboratory is found
    }

    private void assignResearchers(PreparedStatement pstmt) throws SQLException {
        String researcherSQL = "SELECT Researcher_ID FROM Researcher";
        try (Statement researcherStmt = con.createStatement(); ResultSet researcherRs = researcherStmt.executeQuery(researcherSQL)) {
            while (researcherRs.next()) {
                int researcherId = researcherRs.getInt("Researcher_ID");
                int laborId = getRandomLaboratoryWithCapacity(); // Get a random laboratory with capacity
                if (laborId != -1) {
                    pstmt.setInt(1, laborId);
                    pstmt.setInt(2, researcherId);
                    pstmt.setDate(3, getRandomStartDate());
                    pstmt.addBatch();
                    int newCapacity = laboratoryCapacityMap.get(laborId) - 1;
                    laboratoryCapacityMap.put(laborId, newCapacity); // Decrease the capacity
                }
            }
            pstmt.executeBatch();
        }
    }

    private int getRandomLaboratoryWithCapacity() {
        List<Integer> labsWithCapacity = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : laboratoryCapacityMap.entrySet()) {
            if (entry.getValue() > 0) {
                labsWithCapacity.add(entry.getKey());
            }
        }
        if (!labsWithCapacity.isEmpty()) {
            return labsWithCapacity.get(random.nextInt(labsWithCapacity.size()));
        }
        return -1; // Return -1 if no laboratory with capacity is found
    }


    private java.sql.Date getRandomStartDate() {
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.YEAR, -random.nextInt(5)); // Randomly go back up to 5 years( each worker goes back to 5 years)
        calendar.add(Calendar.DAY_OF_YEAR, -random.nextInt(365)); // Randomly go back up to 365 days
        return new java.sql.Date(calendar.getTimeInMillis());
    }
}
