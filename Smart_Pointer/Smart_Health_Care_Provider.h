#pragma once
#include"hospital.h"



class Smart_Health_Care_Provider : public Health_Care_Provider
{
    unsigned fee;
public:
    Smart_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth=500);
    unsigned perform_procedure(unsigned x,std::shared_ptr<Patient> p, Medical_Specialty m);
    std::string hcp_type() const ;
    void receive_license(Medical_Specialty m) override;

};
