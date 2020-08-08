// original problem: https://www.hackerrank.com/challenges/java-string-reverse/copy-from/102690443

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A= sc.next();
        String B = "";
        for(int i =0; i< A.length(); i++){
        char letter = A.charAt(i);
        B = letter + B;
       }
        
    if(A.equals(B)){
      System.out.println("Yes");  
    }
    else{
        System.out.println("No");}
    }
}
