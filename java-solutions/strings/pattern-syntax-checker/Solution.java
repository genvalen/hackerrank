// Original problem: https://www.hackerrank.com/challenges/pattern-syntax-checker/copy-from/107583516

import java.util.Scanner;
import java.util.regex.*;

public class Solution{
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while(testCases>0){
			String pattern = in.nextLine();
          	//Write your code
            try{ 
            Pattern delims = Pattern.compile(pattern);
            System.out.println("Valid");
            }
            catch(PatternSyntaxException ex) 
            { 
            System.out.println("Invalid");  
            } 
            testCases -= 1;
		}
	}
}