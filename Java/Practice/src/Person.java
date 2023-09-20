

import java.util.*;


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
        Person person1 = new Person("Alice", 25);
        Person person2 = new Person("Bob", 30);
        Person person3 = new Person("Charlie", 20);
        Set<Person> set = new TreeSet<>(List.of(person1,person2,person3));
        List<Person> list = new ArrayList<>(List.of(person1,person2,person3));
    }
}
class Student{
    private String name;
    private int iq;

    Student(String name,int iq){
        this.name = name;
        this.iq = iq;
    }
    public String get_name(){
        return name;
    }
    public int getIq(){
        return iq;
    }
    public static Comparator<Student> nameComparator = new Comparator<Student>(){
        @Override
        public int compare(Student lpo, Student rop){
            return lpo.name.compareTo(rop.get_name());
        }
    };

  

    @Override
    public String toString(){
        return "name if the student: " + name + " iq: " + iq;
    }

}
