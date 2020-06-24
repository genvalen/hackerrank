# Original problem: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
if __name__ == '__main__':
    n, s1 = (int(input()), set(input().split()))
    b, s2 = (int(input()), set(input().split()))

    print(len(s1.symmetric_difference(s2)))