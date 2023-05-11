#ifndef TASK_H
#define TASK_H

#include "functional"
#include "vector.h"
#include <algorithm>
#include <numeric>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <stdexcept>
#include <iterator>


enum class Position{Point_Guard,Shooting_Guard,Small_Forward,Power_Forward,Center};
const vector<string> pnamen{"PG","SG","SF","PF","C"};
using namespace std;


Position task1(const Vector<NBA_Player>& v){
  if(v.empty()) throw std::runtime_error("Problem with task 1");
  
  int my count0 = std::count(v.begin(),v.end(),Position::Point_Guard);
  int my count1 = std::count(v.begin(),v.end(),Position::Shooting_Guard);
  int my count2 = std::count(v.begin(),v.end(),Position::Small_Forward);
  int my count3 = std::count(v.begin(),v.end(),Position::Power_Forward);
  int my count4 = std::count(v.begin(),v.end(),Position::Center);
  
  
  
  
  
  
}

//vector<NBA_Player> task2(const Vector<NBA_Player>& v){
//}

//NBA_Player task3(const Vector<NBA_Player>& v,Position c){
//}


//
//
//using sorted_set = 

//sorted_set task6(const Vector<NBA_Player>& v,char s){
//}

//Vector<Team> task7(const Vector<NBA_Player>& v){
//}


#endif
