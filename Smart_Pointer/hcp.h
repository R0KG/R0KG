#pragma once

#include<iostream>
#include<string>
#include<set>
#include<algorithm>
#include"illness.h"
#include"patient.h"
#include<memory>



class Health_Care_Provider {
    std::string n ;
    std::set<Medical_Specialty> topics ;
    unsigned wealth ;
public:
Health_Care_Provider(std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth=500);
std::string get_name() const ;
virtual ~Health_Care_Provider() = default;
void increase_wealth(unsigned x) ;
virtual unsigned perform_procedure(unsigned,std::shared_ptr<Patient>, Medical_Specialty) = 0;

virtual std::string hcp_type() const = 0 ;
bool pay_license(unsigned x) ;
virtual void receive_license(Medical_Specialty x) ;
bool eligible_for(Medical_Specialty m) ;
friend std::ostream& operator<<(std::ostream& o, const Health_Care_Provider& h);


};

