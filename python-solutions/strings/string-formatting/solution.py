# Original problem: https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(n):
    for i in range(1, n+1):
        w = len(bin(n))-2
        print("{0:{width}} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)