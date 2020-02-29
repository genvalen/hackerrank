# Original problem: https://www.hackerrank.com/challenges/input/problem

# Python 2 solution
if __name__=='__main':
    x, k = list(map(int, raw_input().split(" ")))

    # input() in python2 is 
    # equivalent to eval(expression)
    print(input() == k)