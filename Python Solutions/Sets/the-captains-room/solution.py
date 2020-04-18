# Original problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
if __name__ == '__main__':
    k = int(input())
    tourists = list(map(int, input().split()))
    rooms = set(tourists)

    print((sum(rooms)*k - sum(tourists))//(k-1))
    