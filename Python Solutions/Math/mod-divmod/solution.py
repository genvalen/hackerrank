# Original problem: https://www.hackerrank.com/challenges/python-mod-divmod/problem
if __name__ == '__main__':
    a, b = int(input()), int(input())
    print(a//b, a % b, divmod(a, b), sep = '\n')
    