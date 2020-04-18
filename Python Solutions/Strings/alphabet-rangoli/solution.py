# Original problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string

def print_rangoli(n):
    a = list(string.ascii_lowercase)
    l = []

    for i in range(n):
        s = a[i:n] 
        s = "-".join(s[::-1] + s[1:]).center(4*n-3, "-")
        l.append(s)

    print(*l[::-1], *l[1:], sep="\n")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)