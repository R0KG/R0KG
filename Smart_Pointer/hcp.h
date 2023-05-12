#ifndef HPC_H
#define HPC_H

#include<iostream>
#include<stdexcept>
#include<set>
#include<vector>
#include<memory>
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

class Teaching_Health_Care_Provider : public Health_Care_Provider
{
    unsigned fee;
public:
    Teaching_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth=500);
    unsigned perform_procedure(unsigned x,std::shared_ptr<Patient> p, Medical_Specialty m) override;
    std::string hcp_type() const override ;
    bool teach(Medical_Specialty m,std::shared_ptr<Health_Care_Provider> target);

};

  
class Smart_Health_Care_Provider : public Health_Care_Provider
{
    unsigned fee;
public:
    Smart_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth=500);
    unsigned perform_procedure(unsigned x,std::shared_ptr<Patient> p, Medical_Specialty m) override;
    std::string hcp_type() const override ;
    void receive_license(Medical_Specialty m) override;
    unsigned get_fee() const;

};

class Semi_Smart_HCP : public Smart_Health_Care_Provider
{
private:
    bool used = false;
public:
    Semi_Smart_HCP(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth=500);
    void receive_license(Medical_Specialty m) override;



};



#endif
