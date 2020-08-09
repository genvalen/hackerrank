// Original problem: https://www.hackerrank.com/challenges/java-string-tokens/problem

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        // Write your code here.
        if(s.trim().length() == 0 || s.trim().length() > 400000){
            System.out.println(0);
            return;
        }

        else{
            String[] tokens = s.trim().split("[ !,?._'@]+");
            System.out.println(tokens.length);

            for(String word:tokens) {
            System.out.println(word);
            }
        }
        
        scan.close();
    }
}