import java.time.LocalDate;
import java.util.*;
record Employee(String name, int numWork) {}

public class Main{
    public static void main(String [] args){
        Employee emp1 = new Employee("John", 40);
        Employee emp2 = new Employee("Alice", 35);
        Employee emp3 = new Employee("Bob", 42);
        Employee emp4 = new Employee("Sarah", 38);
        Employee emp5 = new Employee("Michael", 37);
        Employee emp6 = new Employee("Emma", 39);
        Employee emp7 = new Employee("David", 41);
        Employee emp8 = new Employee("Olivia", 36);
        Employee emp9 = new Employee("Daniel", 43);
        Employee emp10 = new Employee("Sophia", 34);
        List<Employee> employees = new ArrayList<>(Arrays.asList(emp1,emp2,emp3,emp4,emp5,emp6,emp7,emp8,emp9,emp10));
        printEmplyees(employees);
        
    }
    public static void printEmplyees(List<Employee>list){
        int currentYear = LocalDate.now().getYear();
        class MyEmployee{
            Employee current;
            int years;
            MyEmployee(Employee currentEmployee){
                this.current = currentEmployee;
                years = currentYear;
            }   
            @Override
            public String toString(){
                return "Years: " + years;    
            }

        }
        List<MyEmployee> list2 = new ArrayList<>(list.size());
        for(Employee emp : list){
            list2.add(new MyEmployee(emp));
        }

        var Comp = new Comparator<MyEmployee>(){
            @Override
            public int compare(MyEmployee lop, MyEmployee rop){
                return Integer.compare(lop.years, rop.years);
            }
        };
        list2.sort(Comp);
        System.out.println(list2);
    }
}
