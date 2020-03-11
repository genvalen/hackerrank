# Original problem: https://www.hackerrank.com/challenges/exceptions/problem
t = int(input())

for i in range(t):
    try:
        a, b = list(map(int, input().split()))
        print(a//b)
    except(ZeroDivisionError) as e:
        print("Error Code:", e)
    except(ValueError) as e:
        print("Error Code:", e)
