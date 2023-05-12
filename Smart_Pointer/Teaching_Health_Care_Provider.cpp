
#include"Teaching_Health_Care_Provider.h"

    Teaching_Health_Care_Provider::Teaching_Health_Care_Provider(unsigned fee,std::string n, const std::set<Medical_Specialty>& topics ,unsigned wealth) : fee{fee},Health_Care_Provider(n,topics,wealth){}
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
    bool Teaching_Health_Care_Provider::teach(Medical_Specialty m,std::shared_ptr<Health_Care_Provider> target)
    {

        if(!(this == target.get() || target->eligible_for(m) || !this->eligible_for(m)))
        {
            if(!target->pay_license(fee))
            {
                target->increase_wealth(fee);
                return false;
            }

        }
       
        increase_wealth(fee);
        target->pay_license(fee);
        target->receive_license(m);
        return true;
    }   





