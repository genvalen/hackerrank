#Original problem: https://www.hackerrank.com/challenges/python-loops/problem
if __name__ == '__main__':
    n = int(input())

    print(*[i**2 for i in range(n) if n>=0], sep = "\n")
