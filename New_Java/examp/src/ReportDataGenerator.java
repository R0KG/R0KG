<<<<<<< HEAD
    import com.github.javafaker.Faker;
    import java.sql.*;
    import java.util.Arrays;
    import java.util.List;
    import java.util.Random;

    public class ReportDataGenerator {
        private Connection con;
        private Faker faker;
        private List<String> scienceTopics;
        private Random random;

        public ReportDataGenerator(Connection con) {
            this.con = con;
            this.faker = new Faker();
            this.random = new Random();
            this.scienceTopics = Arrays.asList(
                    "Biology", "Physics", "Chemistry", "Computer Science", "Mathematics",
                    "Medicine", "Environmental Science", "Engineering", "Astronomy", "Robotics"
            );
        }

        public void generateData(int numberOfReports) throws SQLException {
            String sql = "INSERT INTO Report (Report_ID, Topic, Report_Name) VALUES (?, ?, ?)";
            try (PreparedStatement pstmt = con.prepareStatement(sql)) {
                con.setAutoCommit(false);

                for (int i = 1; i <= numberOfReports; i++) {
                    String topic = scienceTopics.get(random.nextInt(scienceTopics.size()));
                    String reportName = "Report: " + i;

                    pstmt.setInt(1, i);
                    pstmt.setString(2, topic);
                    pstmt.setString(3, reportName);
                    pstmt.addBatch();

                    if (i % 100 == 0 || i == numberOfReports) {
                        pstmt.executeBatch();
                        con.commit();
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
    import java.util.Arrays;
    import java.util.List;
    import java.util.Random;

    public class ReportDataGenerator {
        private Connection con;
        private Faker faker;
        private List<String> scienceTopics;
        private Random random;

        public ReportDataGenerator(Connection con) {
            this.con = con;
            this.faker = new Faker();
            this.random = new Random();
            this.scienceTopics = Arrays.asList(
                    "Biology", "Physics", "Chemistry", "Computer Science", "Mathematics",
                    "Medicine", "Environmental Science", "Engineering", "Astronomy", "Robotics"
            );
        }

        public void generateData(int numberOfReports) throws SQLException {
            String sql = "INSERT INTO Report (Report_ID, Topic, Report_Name) VALUES (?, ?, ?)";
            try (PreparedStatement pstmt = con.prepareStatement(sql)) {
                con.setAutoCommit(false);

                for (int i = 1; i <= numberOfReports; i++) {
                    String topic = scienceTopics.get(random.nextInt(scienceTopics.size()));
                    String reportName = "Report: " + i;

                    pstmt.setInt(1, i);
                    pstmt.setString(2, topic);
                    pstmt.setString(3, reportName);
                    pstmt.addBatch();

                    if (i % 100 == 0 || i == numberOfReports) {
                        pstmt.executeBatch();
                        con.commit();
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
