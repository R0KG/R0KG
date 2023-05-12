#include<iostream>
#include<stdexcept>
#include<map>
#include<vector>
#include<memory>
#include<algorithm>
#include "hcp.h"
#include "illness.h"
#include "patient.h"
Health_Care_Provider::Health_Care_Provider(std::string n, const std::set<Medical_Specialty>& topics ,unsigned wealth) : n{n},topics{topics},wealth{wealth}
{
    if(n.empty()) throw std::runtime_error("Error in contructor HCP");
}

std::string Health_Care_Provider::get_name() const {return n;}
void Health_Care_Provider::increase_wealth(unsigned x){wealth+=x;} 
bool Health_Care_Provider::pay_license(unsigned x)
{
    if(wealth < x) return false;
    wealth-=x;
    return true;
}
void Health_Care_Provider::receive_license(Medical_Specialty x){ topics.emplace(x);}
bool Health_Care_Provider::eligible_for(Medical_Specialty m)
{
        auto find_it = std::find_if(topics.begin(),topics.end(),[m](const Medical_Specialty& elem)
    {
        return elem  == m;
    });
    if(find_it != topics.end()) return true;
    return false;
}
std::ostream& operator<<(std::ostream& o, const Health_Care_Provider& h)
{
    bool first = true;
    o << "[" << h.n << ", {";
    for(auto i : h.topics)
        {   
        if(first){
            o << i;
            first = false;
        } 
        else{
            o << ", " << i;
        }
    }
    o << "}, " << h.wealth << " moneyz, " << h.hcp_type() << "]"; 
    return o;
}
    Teaching_Health_Care_Provider::Teaching_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics ,unsigned wealth) : Health_Care_Provider(n,topics,wealth),fee{fee}{}
    unsigned Teaching_Health_Care_Provider::perform_procedure(unsigned x,std::shared_ptr<Patient> p, Medical_Specialty m)
    {
        if(this->eligible_for(m) && p->requires_treatment_in(m) && p->pay_procedure(x))
        {
            this->increase_wealth(x);
            int num = p->cure(m);
            return num;
        }
        return 0;
    }
    std::string Teaching_Health_Care_Provider::hcp_type() const
    {
        return "Teacher";
    }   
bool Teaching_Health_Care_Provider::teach(Medical_Specialty m, std::shared_ptr<Health_Care_Provider> target) {
    // If this is the target, the target already knows 'm', or this doesn't know 'm', return false
    if(this == target.get() || target->eligible_for(m) || !this->eligible_for(m)) 
        return false;

    // If the target can't afford the license, return false
    if(!target->pay_license(fee))
        return false;

    // If the code has reached here, the teaching can be done
    // Increase the wealth of the teaching provider
    increase_wealth(fee);

    // Give the license to the target
    target->receive_license(m);

    return true;
}
        

Smart_Health_Care_Provider::Smart_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth) : Health_Care_Provider(n,topics,wealth),fee{fee}{}
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
unsigned Smart_Health_Care_Provider::get_fee() const{return fee;}

Semi_Smart_HCP::Semi_Smart_HCP(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics,unsigned wealth) : Smart_Health_Care_Provider(fee,n,topics,wealth){}
void Semi_Smart_HCP::receive_license(Medical_Specialty m)
{
    if(!used)
    {
        used = true;
    }
    else
    {
        used = false;
        Health_Care_Provider::receive_license(m);
        this->increase_wealth(this->get_fee());
    }

}