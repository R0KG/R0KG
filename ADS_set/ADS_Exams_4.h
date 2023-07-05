#ifndef ADS_SET_H
#define ADS_SET_H
// Separate Chaining
#include <functional>
#include <algorithm>
#include <iostream>
#include <stdexcept>

template <typename Key, size_t N = 7>
class ADS_set {
public:
  class Iterator;
  using value_type = Key;
  using key_type = Key;
  using reference = value_type &;
  using const_reference = const value_type &;
  using size_type = size_t;
  using difference_type = std::ptrdiff_t;
  using const_iterator = Iterator;
  using iterator = const_iterator;
  using key_compare = std::less<key_type>;                         
  using key_equal = std::equal_to<key_type>;                       // Hashing
  using hasher = std::hash<key_type>;                              // Hashing
private:
  struct Element{
    key_type data;
    Element * next {nullptr};
  };
  Element ** table{nullptr};
  size_type table_size {0};
  float max_lf{0.7};
  size_type current_size{0};
  void add (const key_type & key);
  Element * locate(const key_type & key) const; 
  size_type h(const key_type & key) const { return hasher{}(key) % table_size;}
  std::pair<key_type,key_type> Historie;
  bool was_inserted = false;
public:
  ADS_set() : table{new Element *[N+1]},table_size{N}, current_size{0} {
    for(size_t i = 0;i < N+1;++i){ table[i] = nullptr;}
  }                                                           // PH1
  ADS_set(std::initializer_list<key_type> ilist) : ADS_set{} {insert(ilist);}                   // PH1
  template<typename InputIt> ADS_set(InputIt first, InputIt last) : ADS_set{} {insert(first,last);}     // PH1
  ADS_set(const ADS_set &other);

  ~ADS_set();

  ADS_set &operator=(const ADS_set &other);
  ADS_set &operator=(std::initializer_list<key_type> ilist);

  size_type size() const {return current_size;}                                              // PH1
  bool empty() const{ return current_size == 0;}                                                  // PH1

  void insert(std::initializer_list<key_type> ilist) {insert(ilist.begin(),ilist.end());}                  // PH1
  std::pair<iterator,bool> insert(const key_type &key);
  template<typename InputIt> void insert(InputIt first, InputIt last); // PH1

  void clear();
  size_type erase(const key_type &key);

  size_type count(const key_type &key) const;                          // PH1
  float count_load_factor()const;
  iterator find(const key_type &key) const;

  void swap(ADS_set &other);

  const_iterator begin() const{
    Element ** bucket_ptr = table;
    while(bucket_ptr != &table[table_size] && *bucket_ptr == nullptr){
      ++bucket_ptr;
    }
    return const_iterator{bucket_ptr,*bucket_ptr,&table[table_size]};
  }
  const_iterator end() const{ return const_iterator{&table[table_size],nullptr,&table[table_size]};}
  void dump(std::ostream &o = std::cerr) const;
  void reserve();
  friend bool operator==(const ADS_set &lhs, const ADS_set &rhs)
  {
    if(lhs.current_size != rhs.current_size) return false;
    for(auto lhs_it = lhs.begin(); lhs_it != lhs.end(); ++lhs_it){
      if(rhs.count(*lhs_it) != 1) return false;

    }
  return true;
  }
  friend bool operator!=(const ADS_set &lhs, const ADS_set &rhs){ return !(lhs == rhs);}
  std::pair<key_type,key_type> x() const;
};  
    template <typename Key, size_t N>
    std::pair<typename ADS_set<Key,N>::key_type,typename ADS_set<Key,N>::key_type> ADS_set<Key,N>::x() const{
        if(!was_inserted) throw std::runtime_error("");
        return Historie;
    }

    template <typename Key, size_t N>
    void ADS_set<Key,N>::swap(ADS_set &other){
      std::swap(Historie,other.Historie);
      std::swap(table,other.table);
      std::swap(table_size,other.table_size);
      std::swap(current_size,other.current_size);
    }
    template <typename Key, size_t N>
    typename ADS_set<Key,N>::iterator ADS_set<Key,N>::find(const key_type &key) const{
      if(locate(key)) return Iterator(&table[h(key)],locate(key),&table[table_size]);
      return end();
    }

    template <typename Key, size_t N>
    typename ADS_set<Key,N>::size_type ADS_set<Key,N>::erase(const key_type &key){
      if(!locate(key)) return 0;
      size_type index {h(key)};
      Element * current = table[index];
      Element * prev = nullptr;
      while(current != nullptr){
        if(key_equal{}(current->data,key)){
          if(prev){
            prev->next = current->next;
          }
          else{
            table[index] = current->next;
          }
          delete current;
          --current_size;
          return 1;
        }
        prev = current;
        current = current->next;
      }
      return 0;
    }

      template <typename Key, size_t N>
      void ADS_set<Key,N>::clear(){
        ADS_set temp;
        auto temp_pair = Historie;
        swap(temp);
        Historie = temp_pair;
    }
    
    template <typename Key, size_t N>
    std::pair<typename ADS_set<Key,N>::iterator,bool> ADS_set<Key,N>::insert(const key_type &key)
    {
      was_inserted = true;
        if(key_compare{}(key,Historie.first)){
            Historie.first = key;
        }
        if(key_compare{}(Historie.second,key)){
            Historie.second = key;
        }
      if(!count(key)){
        add(key);
        Iterator res = Iterator(&table[h(key)],locate(key),&table[table_size]);
        return std::make_pair(res,true);
      }
      Iterator res = Iterator(&table[h(key)],locate(key),&table[table_size]);
      
      return std::make_pair(res,false);
    }

    template <typename Key, size_t N>
    ADS_set<Key,N> &ADS_set<Key,N>::operator=(std::initializer_list<key_type> ilist) // maybe need to use std::swap
    {
      ADS_set tmp{ilist};
      swap(tmp);
      return *this;
    }
    template <typename Key, size_t N>
    ADS_set<Key,N> & ADS_set<Key,N>::operator=(const ADS_set &other)// maybe need to use std::swap
    {
        ADS_set tmp{other};
        swap(tmp);
        return *this;
    }
      
    template <typename Key, size_t N>
    ADS_set<Key,N>::~ADS_set(){
      for(size_type i = 0; i < table_size;++i)
      {
        Element * node = table[i];
        while(node){
          Element * next_node = node->next;
          delete node;
          node = next_node;
        }
      }
      delete [] table;
    }

    template <typename Key, size_t N>
    ADS_set<Key,N>::ADS_set(const ADS_set &other) 
    {
      Historie = other.Historie;
      table_size = other.table_size;
      current_size = other.current_size;
      table = new Element *[table_size+1];
      table[table_size] = nullptr;
      for(size_type i = 0;i < table_size;i++) 
      {
        if(other.table[i] == nullptr) table[i] = nullptr;
        else
        {
          Element * other_current = other.table[i];
          table[i] = new Element{other_current->data,nullptr};
          Element * this_current = table[i];
          while(other_current->next != nullptr)
          {
            other_current = other_current->next;
            this_current->next = new Element {other_current->data,nullptr};
            this_current = this_current->next;
          }

        }
      }
    }
    template <typename Key, size_t N>
    void ADS_set<Key,N>::reserve()
    {
      if(this->count_load_factor() <= max_lf) return;
      size_type old_size = table_size;
      while(this->count_load_factor() > max_lf)++(table_size*=2);
      Element ** new_table = new Element *[table_size+1];
      for(size_type index{0};index < table_size+1;index++) new_table[index] = nullptr;
      for(size_type index = 0; index < old_size;index++)
      {
        Element * current = table[index];
        while(current!=nullptr)
        {
          Element * next = current->next;
          size_type new_hash = h(current->data);
          current->next = new_table[new_hash];
          new_table[new_hash] = current;
          current = next;
        }
      }
      delete[] table;
      table = new_table;
    }
    template <typename Key, size_t N>
    float ADS_set<Key,N>::count_load_factor()const
    {
      return current_size/(float)table_size;
    }
    template <typename Key, size_t N>
    void ADS_set<Key,N>::add(const key_type & key)
    {   
        if(!this->locate(key))
        {
        Element * new_elem = new Element{key,nullptr};
        size_type index {h(key)};
        if(table[index] != nullptr)
        {
            new_elem->next = table[index];
        }
        table[index] = new_elem;
        current_size++;
        reserve();
        }
    }
    template<typename Key, size_t N>
    template<typename InputIt> void  ADS_set<Key,N>::insert(InputIt first, InputIt last)
    {
      for(auto it = first; it != last;it++)
      {
        this->add(*it);
        this->reserve();
      }
    }
    template<typename Key, size_t N>
    typename ADS_set<Key,N>::size_type ADS_set<Key,N>::count(const key_type &key) const
    {
      Element * ptr_key = this->locate(key);
      if(ptr_key) return 1;
      return 0;
    }
    
    template<typename Key, size_t N>
    typename ADS_set<Key,N>::Element * ADS_set<Key,N>::locate(const key_type & key) const 
    {
      size_type index{h(key)};
      if(index >= table_size) return nullptr;
      Element * current = table[index];
      while(current != nullptr)
      {
        if(key_equal{}(current->data,key)) return current;
        current = current->next;
      }
      return nullptr;
    }
    template<typename Key, size_t N> 
    void  ADS_set<Key,N>::dump(std::ostream & o) const
    {
      o << "table_size = " << table_size <<", current_size = " << current_size <<", load factor = " << this->count_load_factor() <<"\n";
      for(size_type index{0}; index < table_size;index++)
      {
        if(table[index] != nullptr)
        {
          o << index << "   " << "NNULL" << "-->" << "  ";
          Element * temp_ptr = table[index];
          o << temp_ptr->data << "-->";
          while(temp_ptr != nullptr)
          {
            temp_ptr = temp_ptr->next;
            if(temp_ptr != nullptr) o << temp_ptr->data << "-->";
            else o << "NULL";
          }
        }
        else{
          o << index << "   " << "NULL";
        }
        o << "\n";
      }
    }


template <typename Key, size_t N>
class ADS_set<Key,N>::Iterator {
private:
  Element ** bucket;
  Element * node;
  Element ** end_bucket;
  void skip()
  {
    while(bucket != end_bucket && (node == nullptr))
    {
      ++bucket;
      if(bucket != end_bucket) node = *bucket; 
    }
    
  }
public:
  using value_type = Key;
  using difference_type = std::ptrdiff_t;
  using reference = const value_type &;
  using pointer = const value_type *;
  using iterator_category = std::forward_iterator_tag;

  explicit Iterator(Element ** bucket = nullptr,Element * node = nullptr,Element ** end_bucket = nullptr) : bucket{bucket},node{node},end_bucket{end_bucket} 
  { 
    if(bucket){
      if(node){
        this->node = node;
      }
      else{
        this->node = *bucket;
      }
  }
  skip();
    

  }
  reference operator*() const 
  {
    if(node == nullptr) throw std::runtime_error("Error with reference operator()");
    return node->data;
  }
  pointer operator->() const
  {
    if(node == nullptr) throw std::runtime_error("Error with reference operator()");
    return &(node->data);
  }
  Iterator &operator++()
  {
    if(node)
    {
      node = node->next;
    }
    skip();
    return *this;
  } 
  Iterator operator++(int)
  {
    Iterator old = *this;
    ++*this;
    return old;
  }
  inline friend bool operator==(const Iterator &lhs, const Iterator &rhs) {return lhs.node == rhs.node;}
  inline friend bool operator!=(const Iterator &lhs, const Iterator &rhs) {return lhs.node != rhs.node;}
};

template <typename Key, size_t N>
void swap(ADS_set<Key,N> &lhs, ADS_set<Key,N> &rhs) { lhs.swap(rhs); }

#endif // ADS_SET_H