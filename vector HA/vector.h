#pragma once 
#include<iostream>
#include<string>



class Vector{
public:
class ConstIterator;
class Iterator;
using value_type = double;
using size_type = std::size_t;
using difference_type = std::ptrdiff_t;
using reference = value_type&;
using const_reference = const value_type&;
using pointer = value_type * ;
using const_pointer = const value_type*;
using iterator = Vector::Iterator;
using const_iterator = Vector::ConstIterator;

private:
    size_type sz;
    value_type * values;
    size_type max_sz;
    
public:
    Vector()
    : sz{0},values{new value_type[10]},max_sz{10}{}    
    Vector(size_type n)
    : sz{n},values{new value_type[n+10]},max_sz{n+10}{
      
    }
    Vector(std::initializer_list<value_type> list){
    sz = list.size(); 
    max_sz = sz;
    values = new value_type[max_sz];
    std::copy(list.begin(),list.end(),values);
}
    Vector (const Vector & vec){
    if(vec.sz == 0){
        sz = 0;
        max_sz = 10;
        values = new value_type[max_sz];
    }
    else{
    
    sz = vec.sz;
    max_sz = vec.max_sz;
    values = new value_type[max_sz];
    for(size_t i = 0; i < sz;i++){
        values[i] = vec.values[i];
        }
    }
}
    Vector & operator=(const Vector & rhs){
    if(this == &rhs){
        return *this;
    }
    delete [] values;
    sz = 0;
    sz = rhs.sz;
    max_sz = rhs.max_sz;
    values = new value_type[max_sz];
    for(size_t i = 0; i < sz; i++){
        values[i] = rhs.values[i];
    }
    return *this;
}
    size_t size() const{return sz;}
    bool empty() const {
        if(sz == 0) return true;
        return false;
    }
    void clear(){
        delete[] values;
        sz = 0;
        
    }
    void reserve(size_t n){
        if(max_sz < n){
            max_sz = n;
            value_type * temp = new value_type[max_sz];
            for(size_t i = 0; i < sz;i++){
              temp[i] = values[i];
            }
            delete [] values;
            values = temp;
        }
    }
    void shrink_to_fit()
    { 
      max_sz = sz;
      value_type * temp = new value_type[sz];
      for(size_type i = 0; i < sz;i++){
        temp[i] = values[i];
      }
      delete [] values;
      values = temp;
    }
    void push_back( value_type x){
      if(max_sz <= sz){
      this->reserve(max_sz*2 + 1);
      values[sz] = x;
      }
      else{
        values[sz] = x;
      }

      sz++;
    }   




void pop_back(){
    if(sz == 0){
        throw std::runtime_error("Leer vector");
    }
    
    value_type * temp = new value_type[max_sz-1];
    for(size_type i = 0; i < sz-1;i++){
        temp[i] = values[i];
    }
    sz--;
    --max_sz;
    delete [] values;
    values = temp;
}

value_type &operator[](size_t index){
    if(index > sz-1) throw std::runtime_error("Error with operator[]");
    return values[index];

}
const value_type & operator[](size_t index) const{
    if(index > sz-1) throw std::runtime_error("Error with operator[]");
    return values[index];
}
    
    size_t capacity() const{return max_sz;}
    
~Vector(){
    delete[] values;
}

  iterator end(){
    return iterator(values + sz,values + sz);
  }
  iterator begin(){
    if(this->empty()){
        return this->end();
    }
    return iterator(values,values + sz);
  }
  const_iterator end() const{
    return const_iterator(values+sz,values + sz);
  }
  const_iterator begin() const{
    if(this->empty()){
        return this->end();
    }
    return const_iterator(values,values + sz);
  }
  


class Iterator
{
public:
using value_type = Vector::value_type;
using reference = Vector::reference;
using pointer = Vector::pointer;
using difference_type = Vector::difference_type;
using iterator_category = std::forward_iterator_tag;
private:
//Instanzvariablen
  pointer ptr;
  pointer _end;
public:
//Methoden
  Iterator() : ptr{nullptr},_end{nullptr}{
  }
  Iterator(pointer ptr) :  ptr{ptr},_end{ptr}{
  }
  Iterator(pointer ptr,pointer _end) :  ptr{ptr},_end{_end}{
  }
  reference operator*() const 
  { 
    if(ptr == _end){
      throw std::runtime_error("Problem with operator *");
    }
    
    return *ptr;
  }
  pointer operator->() const
  {
    if(ptr == _end){
      throw std::runtime_error("Problem with operator *");
    }
    return ptr;
  }

  friend bool operator==(const Iterator& lop, const Iterator& rop) {return (lop.ptr == rop.ptr);}
  friend bool operator!=(const Iterator& lop, const Iterator& rop) {return (lop.ptr != rop.ptr);}
   friend Vector::difference_type operator-(const Vector::Iterator& lop, const Vector::Iterator& rop) {
  return lop.ptr - rop.ptr;
}
  iterator& operator++()
  {
    if(ptr == _end){
      return *this;
    }
    ++ptr;
  return (*this);
  }
  iterator operator++(int)
  {
    if(ptr == _end){
      return *this;
    }
    iterator temp(*this);
    ++(*this);
    return temp;
  }
  operator const_iterator(){
    return ConstIterator(ptr,_end);
  }

};

class ConstIterator
{
public:
using value_type = Vector::value_type;
using reference = Vector::const_reference;
using pointer = Vector::const_pointer;
using difference_type = Vector::difference_type;
using iterator_category = std::forward_iterator_tag;
private:
//Instanzvariablen
  pointer ptr;
  pointer _end;
public:
//Methoden
  ConstIterator() : ptr{nullptr},_end{nullptr}{
  }
  ConstIterator(pointer ptr) :  ptr{ptr},_end{ptr}{
  }
  ConstIterator(pointer ptr,pointer _end) :  ptr{ptr},_end{_end}{
  }
  reference operator*() const{
    if(ptr == _end){
      throw std::runtime_error("Problem with operator *");
    }
    return *ptr;
    }
  pointer operator->() const{
    if(ptr == _end){
      throw std::runtime_error("Problem with operator *");
    }
    return ptr;
    }
  friend bool operator==(const ConstIterator& lop, const ConstIterator& rop) {return (lop.ptr == rop.ptr);}
  friend bool operator!=(const ConstIterator& lop, const ConstIterator& rop) {return (lop.ptr != rop.ptr);}
  const_iterator& operator++() {
    if(ptr == _end){
      return *this;
    }
    ++ptr;
    return *this;
  }
  const_iterator operator++(int) {
    if(ptr == _end){
      return *this;
    }
    const_iterator temp(*this);
    ++ptr;
    return temp;
  }
  friend Vector::difference_type operator-(const Vector::ConstIterator& lop, const Vector::ConstIterator& rop) {
  return lop.ptr - rop.ptr;
}
};


iterator insert(const_iterator pos, const_reference val) {
  auto diff = pos - begin();
  if (diff < 0 || static_cast<size_type>(diff) > sz)
    throw std::runtime_error("Iterator out of bounds");
  size_type current{static_cast<size_type>(diff)};
  if (sz >= max_sz)
    reserve(max_sz * 2); // Achtung Sonderfall, wenn keine Mindestgroesze definiert ist
  for (auto i{sz}; i-- > current;)
    values[i + 1] = values[i];
  values[current] = val;
  ++sz;
  return iterator{values + current,values+sz};
}
iterator erase(const_iterator pos) {
  auto diff = pos - begin();
  if (diff < 0 || static_cast<size_type>(diff) >= sz)
    throw std::runtime_error("Iterator out of bounds");
  size_type current{static_cast<size_type>(diff)};
  for (auto i{current}; i < sz - 1; ++i)
    values[i] = values[i + 1];
  --sz;
  return iterator{values + current,values+sz};
}
  
friend std::ostream & operator <<(std::ostream & output,const  Vector& rhs){
    output << "[";
    for(size_t i = 0; i < rhs.size();i++){
        output << rhs.values[i] << ",";
    }
    output << "]";
    return output;
}
};  



   class Iterator
{
  public:
  using value_type = Vector:: value_type;
  using reference = Vector:: reference;
  using pointer = Vector:: pointer;
  using difference_type = Vector:: difference_type;
  using iterator_category = std:: forward_iterator_tag;
  private:
  //Instance variables
  pointer ptr;
  public: 
  // Member functions
    
 Iterator(): ptr{nullptr}
 {
  
 }
  
 Iterator(pointer ptr_in): ptr{ptr_in}
 {
  
 }
  
 reference operator*()const // Iteration
 {
   return *ptr;
 }
  
 pointer operator->()const
 {
   return ptr;
 }
  
 bool operator==(const const_iterator& rop)const
 {
   return rop == *this;
 }
  
 bool operator!=(const const_iterator& rop)const
 {
   return !(*this == rop);
 }
  
 Iterator& operator++()
 {
  ++ptr;
  return *this;
 }
  
 Iterator operator++(int)
 {
  Iterator temp = *this;
  ++(*this);
  return temp;
 }
  
 operator ConstIterator() const
 {
   return ConstIterator(ptr);
 }
};




    




