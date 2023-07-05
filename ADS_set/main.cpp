#include <iostream>
#include <vector>
#include <algorithm>
#include<cassert>
#include "ADS_Exams_9.h" // assuming that ADS_set is the name of your set class

int main() {
  ADS_set<int> test = {4,7,1,5,3,6,0,8,10,2,9};
  auto it = test.begin();
  std::cout << *it;
  std::cout << *(++it);
  ++it;

  return 0;
}