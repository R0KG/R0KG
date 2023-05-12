#pragma once

#include <iostream>
#include <string>
enum class Medical_Specialty {Cardiology,Dermatology,Endocrinology,Gynecology, Neurology,Oncology,Pathology,Pediatrics,Pulmonology,Urology};
extern std::string Spicialty_names[];
std::ostream & operator << (std::ostream & o, Medical_Specialty m);

class Illness {
    Medical_Specialty med;
    std::string name;
public:
    Illness(Medical_Specialty med,const std::string& name);  
    Medical_Specialty get_specialty() const;
    std::string get_name() const;
    friend std::ostream& operator <<(std::ostream& o, const Illness& ill);
    friend bool operator==(const Illness & lhs,const Illness & rhs) ;
    friend bool operator < (const Illness & lhs,const Illness & rhs) ;
};
