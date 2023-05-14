#ifndef ADS_SET_H
#define ADS_SET_H

// ADS_set.h Double Hashing
// 
// VU Algorithmen und Datenstrukturen - SS 2023 Universitaet Wien
// https://cewebs.cs.univie.ac.at/algodat/ss23/
//
// Beispielimplementierung mit "Double Hashing - Linear Probing" 
// Erstellt in der Lehrveranstaltung im SS 2022 
// 29.04.2022 (1. Projektphase)
// 13.05.2022 (2. Projektphase)
//
// Nicht optimiert und eventuell fehlerhaft (Fehler bitte melden)
//
// Die Zurverfügungstellung des Programmes oder Teilen davon auf anderen Plattformen,
// Repositories, etc. ist nicht zulässig.
//
// Dringende Empfehlung: Verwenden Sie diese Implementierung NICHT als 
// Kopiervorlage für Ihre eigene Implementierung! Entwickeln Sie Ihre eigene 
// Implementierung von Grund auf neu.

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
  //using key_compare = std::less<key_type>;                         // B+-Tree
  using key_equal = std::equal_to<key_type>;                       // Hashing
  using hasher = std::hash<key_type>;                              // Hashing

private:
  enum class Mode {free, used, freeagain, end};
  struct Element {
    key_type key;
    Mode mode {Mode::free};
  };
  Element *table {nullptr};
  size_type table_size {0};
  size_type current_size {0};
  float max_lf {0.7};
  
  Element *add(const key_type &key);
  Element *locate(const key_type &key) const;
  size_type h(const key_type &key) const { return hasher{}(key) % table_size; }
  size_type g(const key_type &) const { return 1; }
  void reserve(size_type n);
  void rehash(size_type n);
public:
  ADS_set() { rehash(N); }
  ADS_set(std::initializer_list<key_type> ilist): ADS_set{} { insert(ilist); }
  template<typename InputIt> ADS_set(InputIt first, InputIt last): ADS_set{} { insert(first,last); }
  ADS_set(const ADS_set &other);

  ~ADS_set() { delete[] table; }

  ADS_set &operator=(const ADS_set &other);
  ADS_set &operator=(std::initializer_list<key_type> ilist);

  size_type size() const { return current_size; }
  bool empty() const { return current_size == 0; }

  void insert(std::initializer_list<key_type> ilist) { insert(ilist.begin(), ilist.end()); }
  std::pair<iterator,bool> insert(const key_type &key);
  template<typename InputIt> void insert(InputIt first, InputIt last);

  void clear();
  size_type erase(const key_type &key);

  size_type count(const key_type &key) const { return locate(key) != nullptr; }
  iterator find(const key_type &key) const;

  void swap(ADS_set &other);

  const_iterator begin() const { return const_iterator{table}; }
  const_iterator end() const { return const_iterator{table+table_size}; }
#if TEST == 'z'
  const_iterator z() const { return const_iterator{table,current_size/2,current_size-current_size/2-1}; }
#elif TEST == 'y'
  const_iterator y() const { return current_size < 3 ? end() : const_iterator{table,current_size/3,current_size-current_size/3}; }
#elif TEST == 'x'
  const_iterator x() const { return const_iterator{table,current_size-current_size/4,current_size/4}; }
#endif

  void dump(std::ostream &o = std::cerr) const;

  friend bool operator==(const ADS_set &lhs, const ADS_set &rhs) {
    if (lhs.current_size != rhs.current_size) return false;
    for (const auto &k: lhs) if (!rhs.count(k)) return false;
    return true;
  }
  friend bool operator!=(const ADS_set &lhs, const ADS_set &rhs) { return !(lhs == rhs); }
};

template <typename Key, size_t N>
void ADS_set<Key,N>::swap(ADS_set &other) {
  using std::swap;
  swap(table, other.table);
  swap(table_size, other.table_size);
  swap(current_size, other.current_size);
  swap(max_lf, other.max_lf);
}

template <typename Key, size_t N>
typename ADS_set<Key,N>::iterator ADS_set<Key,N>::find(const key_type &key) const {
  if (auto e {locate(key)}) return iterator{e};
  return end();
}

template <typename Key, size_t N>
typename ADS_set<Key,N>::size_type ADS_set<Key,N>::erase(const key_type &key) {
  if (auto e {locate(key)}) {
    e->mode = Mode::freeagain;
    --current_size;
    return 1;
  }
  return 0;
}

template <typename Key, size_t N>
void ADS_set<Key,N>::clear() {
  ADS_set tmp;
  swap(tmp);
}

template <typename Key, size_t N>
std::pair<typename ADS_set<Key,N>::iterator,bool> ADS_set<Key,N>::insert(const key_type &key) {
  if (auto e {locate(key)}) return {iterator{e},false};
  reserve(current_size+1);
  return {iterator{add(key)},true};
}

template <typename Key, size_t N>
ADS_set<Key,N> &ADS_set<Key,N>::operator=(const ADS_set &other) {
  ADS_set tmp{other};
  swap(tmp);
  return *this;
}

template <typename Key, size_t N>
ADS_set<Key,N> &ADS_set<Key,N>::operator=(std::initializer_list<key_type> ilist) {
  ADS_set tmp{ilist};
  swap(tmp);
  return *this;
}

template <typename Key, size_t N>
ADS_set<Key,N>::ADS_set(const ADS_set &other) {
  rehash(other.table_size);
  for (const auto &k: other) add(k);
}

template <typename Key, size_t N>
typename ADS_set<Key,N>::Element *ADS_set<Key,N>::add(const key_type &key) {
  size_type idx {h(key)}, start_idx{idx};
  while (table[idx].mode == Mode::used) {
    if ((idx = (idx + g(key)) % table_size) == start_idx) throw std::runtime_error{"ADS_set::add: loop detected"};
  }
  table[idx] = {key, Mode::used};
  ++current_size;
  return table+idx; // &table[idx]
}

template <typename Key, size_t N>
typename ADS_set<Key,N>::Element *ADS_set<Key,N>::locate(const key_type &key) const {
  size_type idx {h(key)}, start_idx{idx};
  do {
    switch (table[idx].mode) {
      case Mode::free:
        return nullptr;
      case Mode::used:
        if (key_equal{}(table[idx].key, key)) return table+idx; // return &table[idx];
        break;
      case Mode::freeagain:
        break; 
      case Mode::end:
        throw std::runtime_error{"ADS_set::locate: reached end!"}; 
    }
    idx = (idx + g(key)) % table_size;
  } while (idx != start_idx);
  return nullptr;
}

template <typename Key, size_t N>
template<typename InputIt> void ADS_set<Key,N>::insert(InputIt first, InputIt last) {
  for (auto it {first}; it != last; ++it) {
    if (!count(*it)) {
      reserve(current_size+1);
      add(*it);
    }
  }
}

template <typename Key, size_t N>
void ADS_set<Key,N>::dump(std::ostream &o) const {
  o << "table_size = " << table_size << ", current_size = " << current_size << "\n";
  for (size_type idx {0}; idx < table_size+1; ++idx) {
    o << idx << ": ";
    switch (table[idx].mode) {
      case Mode::free:
        o << "--FREE";
        break;
      case Mode::used:
        o << table[idx].key;
        break;
      case Mode::freeagain:
        o << "--FREEAGAIN";
        break;
      case Mode::end:
        o << "--END";
        break;
    }
    o << "\n";
  }
}

template <typename Key, size_t N>
void ADS_set<Key,N>::reserve(size_type n) {
  if (table_size * max_lf >= n) return;
  size_type new_table_size {table_size};
  while (new_table_size * max_lf < n) ++(new_table_size *= 2);
  rehash(new_table_size);
}

template <typename Key, size_t N>
void ADS_set<Key,N>::rehash(size_type n) {
  size_type new_table_size {std::max(N,std::max(n,size_type(current_size/max_lf)))};
  Element *new_table {new Element [new_table_size+1]};
  new_table[new_table_size].mode = Mode::end;
  Element *old_table {table};
  size_type old_table_size {table_size};
  
  current_size = 0;
  table = new_table;
  table_size = new_table_size;
  
  for (size_type idx {0}; idx < old_table_size; ++idx) {
    if (old_table[idx].mode == Mode::used) add(old_table[idx].key);
  }
  delete[] old_table;
}


template <typename Key, size_t N>
class ADS_set<Key,N>::Iterator {
  Element *e;
  void skip() {
    while (e->mode == Mode::free || e->mode == Mode::freeagain) ++e;
  }
#if TEST == 'z'
  size_t n1{0}, n2{0};
#elif TEST == 'y'
  size_t n1{0}, n2{0};
#elif TEST == 'x'
  size_t n1{0}, n2{0};
#endif
public:
  using value_type = Key;
  using difference_type = std::ptrdiff_t;
  using reference = const value_type &;
  using pointer = const value_type *;
  using iterator_category = std::forward_iterator_tag;

#if TEST == 'z'
  explicit Iterator(Element *e = nullptr, size_t n1 = 0, size_t n2 = 0): e{e}, n1{n1}, n2{n2} { if (e) skip(); }
#elif TEST == 'y'
  explicit Iterator(Element *e = nullptr, size_t n1 = 0, size_t n2 = 0): e{e}, n1{n1}, n2{n2} { if (e) skip(); }
#elif TEST == 'x'
  explicit Iterator(Element *e = nullptr, size_t n1 = 0, size_t n2 = 0): e{e}, n1{n1}, n2{n2} {
    if (e) skip();
    for (auto i{n2}; i; --i) ++*this;
  }
#else
  explicit Iterator(Element *e = nullptr ): e{e} { if (e) skip(); }
#endif
  reference operator*() const { return e->key; }
  pointer operator->() const { return &e->key; }
#if TEST == 'z'
  Iterator &operator++() { 
    do {
      ++e;
      skip();
    } while (!(n1 && --n1) && (n2 && n2--));
    return *this;
  }
/*
  Iterator &operator++() {
    ++e;
    skip();
    if (n1) --n1;
    if (!n1 && n2) {
      while (n2) {
        --n2;
        ++e;
        skip();
      }
    }
    return *this;
  }
  Iterator &operator++() { 
    if (n1) --n1;
    do {
      ++e;
      skip();
    } while (!n1 && n2 && n2--);
    return *this;
  }
*/
#elif TEST == 'y'
  Iterator &operator++() { 
    do {
      ++e;
      skip();
    } while (!(n1 && --n1) && (n2 && n2--));
    return *this;
  }
#elif TEST == 'x'
  Iterator &operator++() { 
    do {
      ++e;
      skip();
    } while (!(n1 && --n1) && (n2 && n2--));
    return *this;
  }
#else
  Iterator &operator++() { ++e; skip(); return *this; }
#endif
  Iterator operator++(int) { auto rc {*this}; ++*this; return rc; }
  friend bool operator==(const Iterator &lhs, const Iterator &rhs) { return lhs.e == rhs.e; }
  friend bool operator!=(const Iterator &lhs, const Iterator &rhs) { return !(lhs == rhs); }
};

template <typename Key, size_t N>
void swap(ADS_set<Key,N> &lhs, ADS_set<Key,N> &rhs) { lhs.swap(rhs); }


#endif // ADS_SET_H