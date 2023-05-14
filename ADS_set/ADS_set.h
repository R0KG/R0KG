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
//   class /* iterator type (implementation-defined) */;
  using value_type = Key;
  using key_type = Key;
  using reference = value_type &;
  using const_reference = const value_type &;
  using size_type = size_t;
  using difference_type = std::ptrdiff_t;
//   using const_iterator = /* iterator type */;
//   using iterator = const_iterator;
//   using key_compare = std::less<key_type>;                         // B+-Tree
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
public:
  ADS_set() : table{new Element *[N]},table_size{N}, current_size{0} {
    for(size_t i = 0;i < N;++i){ table[i] = nullptr;}
  }                                                           // PH1
  ADS_set(std::initializer_list<key_type> ilist) : ADS_set{} {insert(ilist);}                   // PH1
  template<typename InputIt> ADS_set(InputIt first, InputIt last) : ADS_set{} {insert(first,last);}     // PH1
//   ADS_set(const ADS_set &other);

//   ~ADS_set();

//   ADS_set &operator=(const ADS_set &other);
//   ADS_set &operator=(std::initializer_list<key_type> ilist);

  size_type size() const {return current_size;}                                              // PH1
  bool empty() const{ return current_size == 0;}                                                  // PH1

  void insert(std::initializer_list<key_type> ilist) {insert(ilist.begin(),ilist.end());}                  // PH1
//   std::pair<iterator,bool> insert(const key_type &key);
  template<typename InputIt> void insert(InputIt first, InputIt last); // PH1

//   void clear();
//   size_type erase(const key_type &key);

  size_type count(const key_type &key) const;                          // PH1
  float count_load_factor()const;
//   iterator find(const key_type &key) const;

//   void swap(ADS_set &other);

//   const_iterator begin() const;
//   const_iterator end() const;
  void dump(std::ostream &o = std::cerr) const;
  void reserve();

//   friend bool operator==(const ADS_set &lhs, const ADS_set &rhs);
//   friend bool operator!=(const ADS_set &lhs, const ADS_set &rhs);
};  
    template <typename Key, size_t N>
    void ADS_set<Key,N>::reserve()
    {
      if(this->count_load_factor() <= max_lf) return;
      size_type old_size = table_size;
      table_size*=2;
      while(this->count_load_factor() > max_lf)++(table_size*=2);
      Element ** new_table = new Element *[table_size];
      for(size_type index{0};index < table_size;index++) new_table[index] = nullptr;
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
        Element * new_elem = new Element{key,nullptr};
        if(!this->locate(key))
        {
        size_type index {h(key)};
        if(table[index] != nullptr)
        {
            new_elem->next = table[index];
        }
        table[index] = new_elem;
        current_size++;
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


// template <typename Key, size_t N>
// class ADS_set<Key,N>::/* iterator type */ {
// public:
//   using value_type = Key;
//   using difference_type = std::ptrdiff_t;
//   using reference = const value_type &;
//   using pointer = const value_type *;
//   using iterator_category = std::forward_iterator_tag;

//   explicit /* iterator type */(/* implementation-dependent */);
//   reference operator*() const;
//   pointer operator->() const;
//   /* iterator type */ &operator++();
//   /* iterator type */ operator++(int);
//   friend bool operator==(const /* iterator type */ &lhs, const /* iterator type */ &rhs);
//   friend bool operator!=(const /* iterator type */ &lhs, const /* iterator type */ &rhs);
// };

// template <typename Key, size_t N>
// void swap(ADS_set<Key,N> &lhs, ADS_set<Key,N> &rhs) { lhs.swap(rhs); }

#endif // ADS_SET_H