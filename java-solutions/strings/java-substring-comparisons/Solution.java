// Original problem: https://www.hackerrank.com/challenges/java-string-compare/copy-from/101885485

import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0,k);
        String largest = s.substring(0,k);
        for(int i = 0; i < s.length()-(k-1); i++){
            String newString = s.substring(i, i+k);
            if(newString.compareTo(smallest)<0){
                smallest = newString;
            }
            if(newString.compareTo(largest)>0){
                largest = newString;
            }
        } 
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}