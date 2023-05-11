#include<iostream>
#include"vector.h"
using namespace std;

int main() {

  [[maybe_unused]] Vector::value_type val;
  [[maybe_unused]] Vector::size_type size;
  [[maybe_unused]] Vector::difference_type diff;  
  [[maybe_unused]] Vector::reference ref = val;
  [[maybe_unused]] Vector::const_reference cref = val;
  [[maybe_unused]] Vector::pointer ptr = &val;
  [[maybe_unused]] Vector::const_pointer cptr = &val;
  [[maybe_unused]] Vector::iterator *it;
  [[maybe_unused]] Vector::const_iterator *cit;

  return 0;
}
