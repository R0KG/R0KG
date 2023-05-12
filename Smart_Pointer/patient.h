#ifndef PATIENT_H
#define PATIENT_H

#include<iostream>
#include<stdexcept>
#include<set>
#include"illness.h"

class Patient {
    std::string name;
    int age;
    std::set<Illness> illnesses;
    unsigned wealth;
public:
Patient(std::string name ,int age ,const std::set<Illness>& illnesses,unsigned wealth = 200);
void increase_wealth(unsigned x);
bool pay_procedure(unsigned x);
std::string get_name() const;
void catch_disease(const Illness& x);
bool requires_treatment_in(Medical_Specialty x);
bool healthy() const;
unsigned cure(Medical_Specialty x);
friend bool operator==(const Patient & lhs,const Patient & rhs);
friend std::ostream& operator<<(std::ostream& o, const Patient& p);


};


#endif
