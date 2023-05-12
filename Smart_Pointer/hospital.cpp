#include<iostream>
#include<stdexcept>
#include<map>
#include<vector>
#include<memory>
#include<algorithm>
#include "hcp.h"
#include "illness.h"
#include "patient.h"
#include "hospital.h"


Hospital::Hospital(std::string name) : name{name}
{
    if(name.empty()) throw std::runtime_error("Error with constructor Hospital");
}

bool Hospital::sign_hcp(std::shared_ptr<Health_Care_Provider> m)
{
    auto find_it = hcps.find(m->get_name());
    if(find_it == hcps.end()){
        hcps[m->get_name()] = m;
        return true;
    }
    return false;
}
bool Hospital::admit_patient(std::shared_ptr<Patient> m)
{
    auto it_find = patients.find(m->get_name());
    if(it_find == patients.end() || (it_find != patients.end() && it_find->second.expired()))
    {
        patients[m->get_name()] = m;
        return true;
    }
    return false;
}
bool Hospital::dismiss_hcp(std::string n)
{
    for(auto hcp : hcps)
    {
        if(hcp.first == n)
        {
            hcps.erase(n);
            return true;
        }
    }
    return false;
}
std::shared_ptr<Health_Care_Provider> Hospital::get_hcp(std::string n) const
{
    auto it = hcps.find(n);
    if(it == hcps.end()) throw std::runtime_error("Error with get_hcp memeber function (Hospital)");
    return it->second;
}
std::shared_ptr<Patient> Hospital::get_patient(std::string n) const
{
    auto it_find = patients.find(n);
    if( it_find == patients.end() || it_find->second.expired()) throw std::runtime_error("Error with get_patient(Hospital)");
    return it_find->second.lock();
}
bool Hospital::dismiss_patient(std::string n)
{
    auto it_find = patients.find(n);
    if(!it_find->second.expired() && it_find != patients.end())
    {
        patients.erase(n);
        return true;
    }
    else if (it_find->second.expired() && it_find != patients.end())
    {
        patients.erase(n);
        return false;
    } 
    return false;
}
std::ostream& operator<<(std::ostream& o, const Hospital& p)
{
    bool first = true;
    o << "[" << p.name << ", hcps {";
    for(const auto & i : p.hcps)
    {   
        if(first){
            o << *i.second;
            first = false;
        } 
        else{
            o << ", " << *i.second;
        }
    }
  
    o << "}, patients {";
    first = true;
    for(const auto & i : p.patients)
    {
      if(!i.second.expired()){
        if(first){
            o << *i.second.lock();
            first = false;
        } 
        else{
            o << ", " << *i.second.lock();
        }
    }
    }
    o << "}]";
    return o;
}




