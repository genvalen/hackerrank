// Original problem: https://www.hackerrank.com/challenges/java-1d-array-introduction/problem
import java.util.*;
import java.io.*;


class Solution{
    public static void main(String []argh)
    {

        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                //Note: long integer literals must end with 'L'.

                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x>=-128 && x<=127){System.out.println("* byte");}
                if(x>=-32768 && x<=32767){System.out.println("* short");}
                if(x>=-2147483648 && x<=2147483647){System.out.println("* int");} 
                if(x>=-9223372036854775808L && x<=9223372036854775807L)
                    {System.out.println("* long");}

                //ALTERNATIVE using Math.pow(val, pow) notation:

                // long x=sc.nextLong();
                // System.out.println(x+" can be fitted in:");
                // if(x>=-128 && x<=127)System.out.println("* byte");
                // if(x>= Math.pow(2,15)*-1 && x<= Math.pow(2,15)-1) System.out.println("* short");
                // if(x>= Math.pow(2,31)*-1 && x<= Math.pow(2,31)-1)System.out.println("* int");
                // if(x>= Math.pow(2,63)*-1 && x<= Math.pow(3,63)-1)System.out.println("* long");
                
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}