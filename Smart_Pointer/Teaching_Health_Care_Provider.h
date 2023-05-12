#pragma once
#include"hospital.h"



class Teaching_Health_Care_Provider : public Health_Care_Provider
{
    unsigned fee;
public:
    Teaching_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth=500);
    unsigned perform_procedure(unsigned x,std::shared_ptr<Patient> p, Medical_Specialty m);
    std::string hcp_type() const ;
    bool teach(Medical_Specialty m,std::shared_ptr<Health_Care_Provider> target);

};
