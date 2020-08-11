// Original problem: https://www.hackerrank.com/challenges/valid-username-checker/copy-from/107940155
import java.util.Scanner;
import java.util.regex.*;

class UsernameValidator {
    // inset code here
    public static final String regularExpression = "^[A-Z|a-z]\\w{7,29}$";
    Pattern p = Pattern.compile(regularExpression);
}

public class Solution {
    private static final Scanner scan = new Scanner(System.in);
    
    public static void main(String[] args) {
        int n = Integer.parseInt(scan.nextLine());
        while (n-- != 0) {
            String userName = scan.nextLine();

            if (userName.matches(UsernameValidator.regularExpression)) {
                System.out.println("Valid");
            } else {
                System.out.println("Invalid");
            }           
        }
    }
}