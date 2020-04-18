# Original problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
if __name__ == '__main__':
    a, s1 = (input(), set(input().split()))
    b, s2 = (input(), set(input().split()))

    print(len(s1.intersection(s2)))