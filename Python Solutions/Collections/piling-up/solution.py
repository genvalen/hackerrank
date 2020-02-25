# Original problem: https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    d = deque(list(map(int, input().split())))
    cube = max(d[0], d[-1])

    while len(d) >= 0:
        if len(d) == 0:
            print("Yes")
            break

        elif d[0] >= d[-1] and d[0] <= cube:
            cube = d.popleft()

        elif d[-1] >= d[0] and d[-1] <= cube:
            cube = d.pop()
        
        else:
            print("No")
            break
