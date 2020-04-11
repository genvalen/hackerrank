# Original problem: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
if __name__ == '__main__': 
    import re

    n = int(input())
    pattern = r'^[789]\d{9}$'

    for i in range(n):
        match = re.match(pattern, input())
        if match:
            print("YES")
        else:
            print("NO")
        