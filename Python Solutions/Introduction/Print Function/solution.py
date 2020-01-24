#Original problem: https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(input())
    print(*[i+1 for i in range(n)], sep = "")