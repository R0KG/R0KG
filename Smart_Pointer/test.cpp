#include <iostream>
#include <string>
#include <set>
#include <map>
#include <memory>
#include <stdexcept>
#include <sstream>
#include "Illness.h"
#include "Patient.h"
#include "hcp.h"
#include "Hospital.h"
#include "Teaching_Health_Care_Provider.h"
#include "Smart_Health_Care_Provider.h"
#include<cassert>


int main() {
// '    // Test Medical_Specialty
//     std::cout << "Testing Medical_Specialty" << std::endl;
//     std::stringstream ss;
//     ss << Medical_Specialty::Cardiology;
//     if (ss.str() != "Cardiology") {
//         std::cout << "Error: Medical_Specialty::Cardiology is not transformed to Cardiology" << std::endl;
//     }
//     ss.str("");

//     // Test Illness
//     std::cout << "Testing Illness" << std::endl;
//     Illness illness(Medical_Specialty::Cardiology, "Heart Attack");
//     if (illness.get_specialty() != Medical_Specialty::Cardiology || illness.get_name() != "Heart Attack") {
//         std::cout << "Error: Illness initialization or getters not working properly" << std::endl;
//     }
//     ss << illness;
//     if (ss.str() != "[Cardiology, Heart Attack]") {
//         std::cout << "Error: Illness string representation not working properly" << std::endl;
//     }
//     ss.str("");

//     // Test Patient
//     std::cout << "Testing Patient" << std::endl;
//     std::set<Illness> illnesses = {illness};
//     Patient patient("John Doe", 30, illnesses);
//     if (patient.get_name() != "John Doe" || patient.healthy()) {
//         std::cout << "Error: Patient initialization or healthy() function not working properly" << std::endl;
//     }
//     ss << patient;

//     if (ss.str() != "[John Doe, 30 years, {[Cardiology, Heart Attack]}, 200 moneyz]") {
//         std::cout << "Error: Patient string representation not working properly" << std::endl;
//     }
//     ss.str("");

//     // Test Health_Care_Provider
//     std::cout << "Testing Health_Care_Provider" << std::endl;
//     std::set<Medical_Specialty> specialties = {Medical_Specialty::Cardiology};
//     std::shared_ptr<Health_Care_Provider> hcp = std::make_shared<Teaching_Health_Care_Provider>(100, "Dr. Smith", specialties);
//     if (hcp->get_name() != "Dr. Smith") {
//         std::cout << "Error: Health_Care_Provider initialization or get_name() function not working properly" << std::endl;
//     }
//     ss << *hcp;
//     if (ss.str() != "[Dr. Smith, {Cardiology}, 500 moneyz, Teacher]") {
//         std::cout << "Error: Health_Care_Provider string representation not working properly" << std::endl;
//     }
//     ss.str("");

//     // Test Hospital
//     std::cout << "Testing Hospital" << std::endl;
//     Hospital hospital("City Hospital");
//     hospital.sign_hcp(hcp);
//     hospital.admit_patient(std::make_shared<Patient>(patient));
//     std::shared_ptr<Patient> recovered_patient = hospital.get_patient("John Doe");
//     hospital.get_hcp("Dr. Smith")->perform_procedure(100, recovered_patient, Medical_Specialty::Cardiology);
// if (!recovered_patient->healthy()) {
// std::cout << "Error: Patient not cured after procedure" << std::endl;
// }
// ss << hospital;
// if (ss.str() != "[City Hospital, hcps {[Dr. Smith, {Cardiology}, 600 moneyz, Teacher}], patients {[John Doe, 30 years, {}, 100 moneyz]}]") {
// std::cout << "Error: Hospital string representation not working properly" << std::endl;
// }
// ss.str("");
// // Test Teaching_Health_Care_Provider
// std::cout << "Testing Teaching_Health_Care_Provider" << std::endl;
// Teaching_Health_Care_Provider teacher(100, "Dr. Adams", specialties);
// if (teacher.hcp_type() != "Teacher") {
//     std::cout << "Error: Teaching_Health_Care_Provider hcp_type() not working properly" << std::endl;
// }

// // Test Smart_Health_Care_Provider
// std::cout << "Testing Smart_Health_Care_Provider" << std::endl;
// Smart_Health_Care_Provider smart(50, "Dr. Watson", specialties);
// if (smart.hcp_type() != "Smart") {
//     std::cout << "Error: Smart_Health_Care_Provider hcp_type() not working properly" << std::endl;
// }
// smart.receive_license(Medical_Specialty::Dermatology);
// if (!smart.eligible_for(Medical_Specialty::Dermatology) ) {
//     std::cout << "Error: Smart_Health_Care_Provider receive_license() not working properly" << std::endl;
// }

// std::cout << "All tests completed." << std::endl;

// Test Teaching_Health_Care_Provider
 // Test Teaching_Health_Care_Provider
    std::cout << "Testing Teaching_Health_Care_Provider" << std::endl;

    // Create a new Teaching_Health_Care_Provider
    std::set<Medical_Specialty> specialties = {Medical_Specialty::Cardiology};
    Teaching_Health_Care_Provider teacher(100, "Dr. Adams", specialties);

    // Test name
    assert(teacher.get_name() == "Dr. Adams");

    // Test hcp_type
    assert(teacher.hcp_type() == "Teacher");

    // Test eligible_for
    assert(teacher.eligible_for(Medical_Specialty::Cardiology));

    // Test perform_procedure
    Illness illness(Medical_Specialty::Cardiology, "Heart Attack");
    std::set<Illness> illnesses = {illness};
    std::shared_ptr<Patient> patient = std::make_shared<Patient>("John Doe", 30, illnesses);
    assert(teacher.perform_procedure(100, patient, Medical_Specialty::Cardiology) == 1);

    // Test teach
    std::shared_ptr<Teaching_Health_Care_Provider> hcp = std::make_shared<Teaching_Health_Care_Provider>(50, "Dr. Smith", specialties);
    assert(teacher.teach(Medical_Specialty::Cardiology, hcp));

    // Test unsuccessful teach
    std::shared_ptr<Teaching_Health_Care_Provider> hcp2 = std::make_shared<Teaching_Health_Care_Provider>(150, "Dr. Johnson", specialties,10);
    assert(!teacher.teach(Medical_Specialty::Cardiology, hcp2)); // Assuming Dr. Johnson doesn't have enough wealth to pay the fee

    std::cout << "All Teaching_Health_Care_Provider tests passed!" << std::endl;



return 0;
}
