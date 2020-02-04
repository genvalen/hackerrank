# Original problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
a, s1 = (input(), set (input().split()))
b, s2 = (input(), set(input().split()))

print(len(s1.difference(s2)))