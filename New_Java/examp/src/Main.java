import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        String databaseUrl = "jdbc:oracle:thin:@oracle19.cs.univie.ac.at:1521:orclcdb";
        String user = "a11919434";
        String password = "dbs23";

        try {
            Connection con = DriverManager.getConnection(databaseUrl, user, password);

            // University Data Generation
            UniversityDataGenerator_2 universityGenerator = new UniversityDataGenerator_2(con);
            universityGenerator.generateData();

            // Laboratory Data Generation
            LaboratoryDataGenerator labGenerator = new LaboratoryDataGenerator(con);
            labGenerator.generateData();

            // Worker Data Generation
            WorkerDataGenerator workerGenerator = new WorkerDataGenerator(con);
            workerGenerator.generateWorkerData();

            //Researcher Data Generation
            ResearcherDataGenerator researcherGenerator = new ResearcherDataGenerator(con);
            researcherGenerator.generateData();

            // Head Researcher Data Generation
            HeadResearcherDataGenerator headResearcherGenerator = new HeadResearcherDataGenerator(con);
            headResearcherGenerator.generateData();

            //Employs Data Generation
            EmploysDataGenerator employsGenerator = new EmploysDataGenerator(con);
            employsGenerator.generateData();

            //Leads Data Generation
             LeadsDataGenerator leadsGenerator = new LeadsDataGenerator(con);
            leadsGenerator.generateData();

            //Communicates Data Generation
            CommunicatesDataGenerator communicatesGenerator = new CommunicatesDataGenerator(con);
            communicatesGenerator.generateData();

            // Project Data Generation
            ProjectDataGenerator projectGenerator = new ProjectDataGenerator(con);
            projectGenerator.generateData(1000);

            // Report Data Generation
            ReportDataGenerator reportGenerator = new ReportDataGenerator(con);
            reportGenerator.generateData(1000);

            //Makes Data Generation
            MakesDataGenerator makesGenerator = new MakesDataGenerator(con, 2000, 1000, 1000);
            makesGenerator.generateData();

            con.close();
            System.out.println("Data generation completed successfully.");

        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Failed to generate data: " + e.getMessage());
        }
    }
}