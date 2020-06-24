# Original problem: https://www.hackerrank.com/challenges/introduction-to-regex/problem
if __name__ == '__main__':
    import re
    
    for _ in range(int(input())):
        print(bool(re.match(r'^[-+]?\d*\.\d+$', input())))
