#include"hcp.h"

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
    o << "[" << h.n << ", {";
    for(auto i : h.topics){ std::cout << i;}
    o << "}, " << h.wealth << "moneyz, " << h.hcp_type() << "]"; 
    return o;
}