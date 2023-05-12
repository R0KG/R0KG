#include "illness.h"
#include<vector>
#include<string>
#include<iostream>

Illness::Illness(Medical_Specialty med, const std::string &name) : med{med}, name{name} {
    if (name.empty()) throw std::runtime_error("Error with Illness Constructor");
}

Medical_Specialty Illness::get_specialty() const {
    return med;
}

std::string Illness::get_name() const {
    return name;
}

std::ostream &operator<<(std::ostream &o, const Illness &ill) {
    o << "[" << Spicialty_names.at(static_cast<std::size_t>(ill.get_specialty())) << ", ";
    o << ill.get_name() << "]";
    return o;
}

bool operator==(const Illness &lhs, const Illness &rhs) {
    return (lhs.name == rhs.name && lhs.med == rhs.med);
}

bool operator<(const Illness &lhs, const Illness &rhs) {
    if (lhs.med < rhs.med) return true;
    if (lhs.med == rhs.med) {
        return lhs.name < rhs.name;
    }
    return false;
}



std::ostream &operator<<(std::ostream &o, Medical_Specialty m) {
    return o << Spicialty_names.at(static_cast<std::size_t>(m));
}
