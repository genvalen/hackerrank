#Original problem: https://www.hackerrank.com/challenges/symmetric-difference/problem
a, b = (int(input()), set(input().split()))
c, d = (int(input()), set(input().split()))

p = b.difference(d)
q = d.difference(b)

[print(i) for i in sorted(p.union(q), key = int)]