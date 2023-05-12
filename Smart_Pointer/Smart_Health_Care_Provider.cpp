#include "Smart_Health_Care_Provider.h"

Smart_Health_Care_Provider::Smart_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth) : fee{fee},Health_Care_Provider(n,topics,wealth){}
unsigned Smart_Health_Care_Provider::perform_procedure(unsigned x,std::shared_ptr<Patient> p, Medical_Specialty m)
{
    return 0;
}
std::string Smart_Health_Care_Provider::hcp_type() const
{
    return "Smart";
}
void Smart_Health_Care_Provider::receive_license(Medical_Specialty m)
{
    this->increase_wealth(fee);
    this->Health_Care_Provider::receive_license(m);
}