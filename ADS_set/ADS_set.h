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
  size_type current_size{0};
  void add (const key_type & key);
  Element * locate(const key_type) const;
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

  void insert(std::initializer_list<key_type> ilist);                  // PH1
//   std::pair<iterator,bool> insert(const key_type &key);
  template<typename InputIt> void insert(InputIt first, InputIt last); // PH1

//   void clear();
//   size_type erase(const key_type &key);

  size_type count(const key_type &key) const;                          // PH1
//   iterator find(const key_type &key) const;

//   void swap(ADS_set &other);

//   const_iterator begin() const;
//   const_iterator end() const;

  void dump(std::ostream &o = std::cerr) const;

//   friend bool operator==(const ADS_set &lhs, const ADS_set &rhs);
//   friend bool operator!=(const ADS_set &lhs, const ADS_set &rhs);
};

    template <typename Key, size_t N>
    void ADS_set<Key,N>::add(const key_type & key)
    {   
        Element * new_elem = new Element{key,nullptr};
        size_type index {h(key)};
        if(table[index] != nullptr)
        {
            new_elem->next = table[index];
        }
        table[index] = new_elem;
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