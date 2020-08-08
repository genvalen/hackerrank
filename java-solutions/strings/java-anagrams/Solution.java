// Original problem: https://www.hackerrank.com/challenges/java-anagrams/copy-from/103065475

import java.util.Scanner;

public class Solution {

    static int frequency(char a, String b) {
        int frequency = 0;
        Character.toLowerCase(a);
        b.toLowerCase();
        for (int i=0; i<b.length(); i++) {
            if(b.charAt(i) == a){
                frequency++;
            }
        }
        return frequency;
    }
    
    static boolean isAnagram(String a, String b) {
        boolean passTest = true;
        int i = 0;
        a = a.toLowerCase();
        b = b.toLowerCase();

        if(a.length() != b.length()){
            passTest = false;
        }
        
        while(passTest && i < a.length()-1){
            i++;
            if(b.indexOf(a.charAt(i)) == -1){
                passTest = false;
                break;
            }
            else{
                if(frequency(a.charAt(i), a) != frequency(a.charAt(i), b)){
                    passTest = false;
                    break;
                }
            }
        }
        return passTest;    
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}