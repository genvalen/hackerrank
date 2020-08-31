// Original problem: https://www.hackerrank.com/challenges/java-strings-introduction/copy-from/99550701

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        /* Enter your code here. Print output to STDOUT. */

        System.out.println(A.length() + B.length());

        
        int result = A.compareTo(B);
        if(result > 0){
           System.out.println("Yes");     
        }
        else{
            System.out.println("No");
        }


        String firstLetterA = A.substring(0,1).toUpperCase();
        String firstLetterB= B.substring(0,1).toUpperCase();

        String newStringA = firstLetterA + A.substring(1);
        String newStringB = firstLetterB + B.substring(1);

        System.out.println(newStringA +" "+ newStringB);
    }
}
