#include<iostream>
#include<stdexcept>
#include<set>
#include<algorithm>
#include "patient.h"
#include "illness.h"



Patient::Patient(std::string name ,int age ,const std::set<Illness>& illnesses,unsigned wealth): name{name},age{age},illnesses{illnesses},wealth{wealth}
{
    if(name.empty() || age < 0 || illnesses.empty()) throw std::runtime_error("Problem with patient constructor");
}
void Patient::increase_wealth(unsigned x){wealth+=x;}
bool Patient::pay_procedure(unsigned x)
{
    if(wealth < x) return false;
    else wealth-=x;
    return true;
}
void Patient::catch_disease(const Illness& x)
{
    illnesses.emplace(x);
}
bool Patient::requires_treatment_in(Medical_Specialty x)
{
    auto find_it = std::find_if(illnesses.begin(),illnesses.end(),[x](const Illness& elem)
    {
        return elem.get_specialty() == x;
    });
    if(find_it != illnesses.end()) return true;
    return false;
}
bool Patient::healthy() const{
    if(illnesses.empty())return true;
    return false;
    }
    unsigned Patient::cure(Medical_Specialty x)
    {
        unsigned count_illness = std::count_if(illnesses.begin(),illnesses.end(),[x](const Illness& elem)
        {
            return elem.get_specialty() == x;
        });
        auto it_find = std::find_if(illnesses.begin(),illnesses.end(),[x](const Illness& elem)
        {
            return elem.get_specialty() == x;
        });
        while(it_find != illnesses.end())
        {
            illnesses.erase(it_find);
            it_find = std::find_if(illnesses.begin(),illnesses.end(),[x](const Illness& elem)
        {
            return elem.get_specialty() == x;
        });
        }
        return count_illness;
    }
bool operator==(const Patient & lhs,const Patient & rhs)
{
    return (lhs.name == rhs.name && lhs.age == rhs.age && lhs.illnesses == rhs.illnesses && lhs.wealth == rhs.wealth);
}
std::ostream& operator<<(std::ostream& o, const Patient& p)
{
    bool first = true;
    o << "[" << p.name << ", " << p.age <<" years, {";
    for(auto i : p.illnesses)
    {   
        if(first){
            o << i;
            first = false;
        } 
        else{
            o << ", " << i;
        }
    }
    o << "}, " << p.wealth << " moneyz]";
    return o;
}

std::string Patient::get_name() const
{
    return name;
}
