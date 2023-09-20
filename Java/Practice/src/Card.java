import java.util.*;

public class Card{
    public enum Suit {
        CLUB,DIAMOND,HEART,SPADE;
        public char getImage(){
            return (new char[]{9827,9830,9829,9824})[this.ordinal()];
        }
    }
    Suit suit;
    String num;
    String rank;
    Card(Suit suit,String num, String rank){
        this.suit = suit;
        this.num = num;
        this.rank = rank;
    } 
    @Override
    public String toString(){
        int index = num.equals("10") ? 2 : 1;
        String faceString = num.substring(0, index);
        return faceString + suit.getImage() + "(" + rank + ") ";
    }
    public static void main(String [] args){
        Card temp = new Card(Suit.CLUB, "2", "10");
        System.out.println(temp);
    }
}