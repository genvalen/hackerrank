# Original problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
if __name__ == '__main__':
    a = int(input())
    s1 = set(map(int, input().split()))
    t = int(input())

    for i in range(t):
        cmd, *args = input().split()
        s2 = set(map(int, input().split()))
        getattr(s1, cmd)(s2)

    print(sum(s1))