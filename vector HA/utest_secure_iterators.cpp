#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "vector.h"

TEST_CASE("SecureIterator, EndIterator") {
  Vector v({0,1,2,3,4,5,6,7,8,9});
  auto end{v.end()};

  CHECK_NOTHROW( ++end );
  CHECK( end == v.end() );
  CHECK_NOTHROW( end++ );
  CHECK( end == v.end() );
  CHECK_THROWS( *end );
  CHECK_THROWS( end.operator->());

  CHECK_NOTHROW( ++v.end() );
  CHECK( end == ++v.end() );
  CHECK_NOTHROW( v.end()++ );
  CHECK( end == v.end()++ );
  CHECK_THROWS( *v.end() );
  CHECK_THROWS( v.end().operator->());

}

TEST_CASE("SecureConstIterator, EndIterator") {
  const Vector v({0,1,2,3,4,5,6,7,8,9});
  auto end{v.end()};

  CHECK_NOTHROW( ++end );
  CHECK( end == v.end() );
  CHECK_NOTHROW( end++ );
  CHECK( end == v.end() );
  CHECK_THROWS( *end );
  CHECK_THROWS( end.operator->());

  CHECK_NOTHROW( ++v.end() );
  CHECK( end == ++v.end() );
  CHECK_NOTHROW( v.end()++ );
  CHECK( end == v.end()++ );
  CHECK_THROWS( *v.end() );
  CHECK_THROWS( v.end().operator->());

}

TEST_CASE("SecureIterator, IteratorRange") {
  Vector v({0,1,2,3,4,5,6,7,8,9});
	
	auto it{v.begin()};
	for (Vector::size_type i{0}; i<v.size()-1; ++i)
		CHECK_NOTHROW( ++it );
	CHECK( *it == 9);
	CHECK( *(it.operator->()) == 9);
  CHECK_NOTHROW( ++it );
  CHECK( it == v.end()) ;
  CHECK_NOTHROW( ++it );
  CHECK( it == v.end() );
  CHECK_NOTHROW( it++ );
  CHECK( it == v.end() );
  CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->());
}

TEST_CASE("SecureConstIterator, IteratorRange") {
  const Vector v({0,1,2,3,4,5,6,7,8,9});
	
	auto it{v.begin()};
	for (Vector::size_type i{0}; i<v.size()-1; ++i)
		CHECK_NOTHROW( ++it );
	CHECK( *it == 9);
	CHECK( *(it.operator->()) == 9);
  CHECK_NOTHROW( ++it );
  CHECK(it == v.end());
  CHECK_NOTHROW( ++it );
  CHECK(it == v.end());
  CHECK_NOTHROW( it++ );
  CHECK(it == v.end());
  CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->());
}

TEST_CASE("SecureIterator, DefaultIterator") {
	Vector::iterator test;
	CHECK_NOTHROW( ++test );
	CHECK_NOTHROW( test++ );
	CHECK( test == Vector::iterator{} );
	CHECK_THROWS( *test );
	CHECK_THROWS( test.operator->());
}

TEST_CASE("SecureConstIterator, DefaultIterator") {
	Vector::const_iterator test;
	CHECK_NOTHROW( ++test );
	CHECK_NOTHROW( test++ );
	CHECK( test == Vector::const_iterator{} );
	CHECK_THROWS( *test );
	CHECK_THROWS( test.operator->());
}

TEST_CASE("StronglySecuredIterator, RandomPointer") {
  Vector v({0,1,2,3,4,5,6,7,8,9});
  auto start{v.begin()};
  auto stop{v.end()};
  CHECK( *(++start) == 1 );
  CHECK( *((++start).operator->()) ==2 );
  CHECK_NOTHROW( ++stop );
  CHECK_NOTHROW( stop++ );
  CHECK( stop == v.end() );
  CHECK_THROWS( *stop );
  CHECK_THROWS( stop.operator->() );

  double val{3.1415};
  Vector::iterator it{&val};
  std::cout << &val << " " << v.begin().operator->() << '\n';
  CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->() );
  CHECK_NOTHROW( ++it );
  CHECK_NOTHROW( it++ );
  CHECK( it == Vector::iterator{&val} );

  Vector::iterator it1{start.operator->()-10};
  CHECK_THROWS( *it1 );
  CHECK_THROWS( it1.operator->() );
  CHECK_NOTHROW( ++it1 );
  CHECK_NOTHROW( it1++ );
  CHECK( it1 == Vector::iterator{start.operator->()-10} );
}

TEST_CASE("StronglySecuredConstIterator, RandomPointer") {
  const Vector v({0,1,2,3,4,5,6,7,8,9});
  auto start{v.begin()};
  auto stop{v.end()};
  CHECK( *(++start) == 1 );
  CHECK( *((++start).operator->()) ==2 );
  CHECK_NOTHROW( ++stop );
  CHECK_NOTHROW( stop++ );
  CHECK( stop == v.end() );
  CHECK_THROWS( *stop );
  CHECK_THROWS( stop.operator->() );

  double val{3.1415};
  Vector::const_iterator it{&val};
  std::cout << &val << " " << v.begin().operator->() << '\n';
  CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->() );
  CHECK_NOTHROW( ++it );
  CHECK_NOTHROW( it++ );
  CHECK( it == Vector::const_iterator{&val} );

  Vector::const_iterator it1{start.operator->()-10};
  CHECK_THROWS( *it1 );
  CHECK_THROWS( it1.operator->() );
  CHECK_NOTHROW( ++it1 );
  CHECK_NOTHROW( it1++ );
  CHECK( it1 == Vector::const_iterator{start.operator->()-10} );
}

TEST_CASE("StronglySecuredIterator, Realloc") {
  Vector v({0,1,2,3,4,5,6,7,8,9});
  auto it{v.begin()};
  auto orig{it};
  v.reserve(v.capacity()*2);
  CHECK_NOTHROW( ++it );
  CHECK_NOTHROW( it++ );
  CHECK( it == orig );
  CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->());
}

TEST_CASE("StronglySecuredConstIterator, Realloc") {
  Vector v({0,1,2,3,4,5,6,7,8,9});
  Vector::const_iterator it{v.begin()};
  auto orig{it};
  v.reserve(v.capacity()*2);
  CHECK_NOTHROW( ++it );
  CHECK_NOTHROW( it++ );
  CHECK( it == orig );
  CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->());
}

TEST_CASE("StronglySecuredIterator, Insert") {
	Vector v(2);
	v.push_back(7.5);
	auto it{v.begin()};
	v.insert(v.end(),1.2);
	CHECK_NOTHROW( ++it);
	CHECK_NOTHROW( it++);
	CHECK( it == v.end());
	CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->());
}

TEST_CASE("StronglySecuredIterator, Erase") {
	Vector v{1,2};
	auto it{v.begin()};
	auto loc{it};
	CHECK_NOTHROW( ++loc );
	v.erase(loc);
	CHECK_NOTHROW( ++it);
	CHECK_NOTHROW( it++);
	CHECK( it == v.end());
	CHECK_THROWS( *it );
  CHECK_THROWS( it.operator->());
}
