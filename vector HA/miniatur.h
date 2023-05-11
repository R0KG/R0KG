#ifndef MINIATUR_H
#define MINIATUR_H
#include<iostream>
#include<vector>
#include<string>
#include<stdexcept>


enum class Fraktion{Tyraniden,SM,CSM,Orks,AstraMilitarum,GreyKnights,Demons,Harlequins,ThousandSons,AdeptusMechanicus,Craftworlds,Drukhari};

struct EnumClassHash
{
    template <typename T>
    std::size_t operator()(T t) const
    {
        return static_cast<std::size_t>(t);
    }
};

std::string to_s(Fraktion);

class Miniatur{
  std::string name;
  Fraktion f;
  int points;
  public:
    Miniatur(std::string="Hive_Tyrant",Fraktion=Fraktion::Tyraniden,int=180);
    bool change_points(int);
    std::string get_name() const;
    Fraktion get_fraktion() const;
    int get_points() const;
    virtual std::ostream& print(std::ostream&) const; 
    std::ostream& write(std::ostream&) const;
    virtual ~Miniatur() = default;
};

class Spezial_Miniatur : public Miniatur{
  int nr;
  static int counter;
  public:
    Spezial_Miniatur(std::string="Hive_Tyrant",Fraktion=Fraktion::Tyraniden,int=180);
    std::ostream& print(std::ostream& o) const override;
};

std::ostream& operator<<(std::ostream& o,const Miniatur& s);
std::ostream& operator<<(std::ostream& o,const Spezial_Miniatur& s);

#endif
