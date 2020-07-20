// Original problem: https://www.hackerrank.com/challenges/java-end-of-file/problem
import java.io.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = 1;

        while (scan.hasNext()) {
            System.out.println(count + " " + scan.nextLine());
            count++;

        }
    }
}
