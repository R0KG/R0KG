

import java.util.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Person {
    private String name;
    private int age;

    // Constructor, getters, and setters...

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public static Comparator<Person> NameComparator = new Comparator<Person>() {
        @Override
        public int compare(Person person1, Person person2) {
           return person1.name.compareTo(person2.name);
        }
    };

    public static Comparator<Person> AgeComparator = new Comparator<Person>() {
        @Override
        public int compare(Person person1, Person person2) {
           return Integer.compare(person1.age, person2.age);
        }
    };

    @Override
    public String toString() {
        return "Person [name=" + name + ", age=" + age + "]";
    }

    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person("John", 25));
        people.add(new Person("Alice", 22));
        people.add(new Person("Zoe", 20));

        System.out.println("Original list: " + people);

        Collections.sort(people, Person.NameComparator);
        System.out.println("Sorted by Name: " + people);

        Collections.sort(people, Person.AgeComparator);
        System.out.println("Sorted by Age: " + people);
    }
}
