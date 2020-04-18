# Original problem: https://www.hackerrank.com/challenges/py-set-union/problem
if __name__ == '__main__':
    a, s1 = (int(input()), set(input().split()))
    b, s2 = (int(input()), set(input().split()))

    print(len(s2.union(s1)))
