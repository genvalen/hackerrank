# Original problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
a, s1 = (input(), set(input().split()))
b, s2 = (input(), set(input().split()))

print(len(s1.intersection(s2)))