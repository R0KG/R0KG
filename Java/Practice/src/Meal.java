import java.util.*;
public class Meal {

    private double base = 5.0;
     private Item burger;
     private Item drink;
     private Item side;


    private class Item{
        private String name;
        private String type;
        private double price;

        Item(String name, String type , double price){
            this.name = name;
            this.type = type;
            this.price = price;
             
        }

    }
}
