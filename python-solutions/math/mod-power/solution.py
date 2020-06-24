# Original problem: https://www.hackerrank.com/challenges/python-power-mod-power/problem
if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    print(pow(a,b), pow(a, b, c), sep = '\n')
