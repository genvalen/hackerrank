# Original problem: https://www.hackerrank.com/challenges/incorrect-regex/problem
if __name__ == '__main__':
    import re

    t = int(input())
    
    for i in range(t):
        try:
            print(bool(re.compile(input())))
        except re.error:
            print("False")
            