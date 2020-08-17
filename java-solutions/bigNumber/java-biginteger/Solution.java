// Original problem: https://www.hackerrank.com/challenges/java-biginteger/copy-from/107592144
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger a, b;
        a = new BigInteger(scan.next());
        b = new BigInteger(scan.next());
        BigInteger sum = a.add(b);
        BigInteger product = a.multiply(b);

        System.out.println(sum.toString().replaceFirst("^0+(?!$)", "")
         + "\n" + product.toString().replaceFirst("^0+(?!$)", ""));


    }
}

