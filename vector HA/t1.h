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
    size_t sz;
    size_t max_sz;
    value_type * values;
public:
    Vector()
    : sz{0},max_sz{5},values{nullptr}{}    
    Vector(size_t n)
    : sz{0},max_sz{n},values{nullptr}{}
    Vector(std::initializer_list<value_type> list){
    sz = list.size();
    max_sz = sz;
    values = new value_type[sz];
    std::move(list.begin(),list.end(),values);
}
    Vector (const Vector & vec){
    if(vec.sz == 0){
        Vector();
    }
    else{
    sz = vec.sz;
    max_sz = vec.max_sz;
    values = new value_type[sz];
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
    sz = rhs.sz;
    max_sz = rhs.max_sz;
    values = new value_type[sz];
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
        }
    }
    void shrink_to_fit(){ max_sz = sz;}
    void push_back(value_type x){
    value_type * temp = new value_type[sz+1];
    for(size_t i = 0;i < sz;i++){
        temp[i] = values[i];
    }
    temp[sz] = x;
    sz++;
    delete [] values;
    values = temp;
}   



void pop_back(){
    if(sz == 0){
        throw std::runtime_error("Leer vector");
    }
    value_type * temp = new value_type[sz-1];
    for(size_t i = 0; i < sz-1;i++){
        temp[i] = values[i];
    }
    sz--;
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
public:
//Methoden
  Iterator() : ptr{nullptr}{}
  Iterator(pointer ptr) : ptr{ptr}{}
  reference operator*() const 
  {
    return *ptr;
  }
  pointer operator->() const
  {
    return ptr;
  }
  friend bool operator==(const Iterator& lop, const Iterator& rop) {return (*lop.ptr == *rop.ptr);}
  friend bool operator!=(const Iterator& lop, const Iterator& rop) {return (*lop.ptr != *rop.ptr);}
  iterator& operator++()
  {
    ++ptr;
  return (*this);
  }
  iterator operator++(int)
  {
    iterator temp(*this);
    ++(*this);
    return temp;
  }
  operator const_iterator(){
    return ConstIterator(ptr);
  }
   friend Vector::difference_type operator-(const Vector::Iterator& lop, const Vector::Iterator& rop) {
  return lop.ptr - rop.ptr;
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
public:
//Methoden
  ConstIterator () : ptr{nullptr}{}
  ConstIterator (pointer ptr) : ptr{ptr}{}
  reference operator*() const{return *ptr;}
  pointer operator->() const{return ptr;}
  friend bool operator==(const ConstIterator& lop, const ConstIterator& rop) {return (*lop.ptr == *rop.ptr);}
  friend bool operator!=(const ConstIterator& lop, const ConstIterator& rop) {return (*lop.ptr != *rop.ptr);}
  const_iterator& operator++() {
    ++ptr;
    return *this;
  }
  const_iterator operator++(int) {
    const_iterator temp(*this);
    ++ptr;
    return temp;
  }
  friend Vector::difference_type operator-(const Vector::ConstIterator& lop, const Vector::ConstIterator& rop) {
  return lop.ptr - rop.ptr;
}
};
  iterator end(){
    return iterator(values+sz);
  }
  iterator begin(){
    if(this->empty()){
        return this->end();
    }
    return iterator(values);
  }
  const_iterator end() const{
    return const_iterator(values+sz);
  }
  const_iterator begin() const{
    if(this->empty()){
        return this->end();
    }
    return const_iterator(values);
  }
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
  return iterator{values + current};
}
iterator erase(const_iterator pos) {
  auto diff = pos - begin();
  if (diff < 0 || static_cast<size_type>(diff) >= sz)
    throw std::runtime_error("Iterator out of bounds");
  size_type current{static_cast<size_type>(diff)};
  for (auto i{current}; i < sz - 1; ++i)
    values[i] = values[i + 1];
  --sz;
  return iterator{values + current};
}
  
friend std::ostream & operator <<(std::ostream & output,const  Vector & rhs){
    output << "[";
    for(size_t i = 0; i < rhs.size();i++){
        output << rhs.values[i] << ",";
    }
    output << "]";
    return output;
}
};




    




