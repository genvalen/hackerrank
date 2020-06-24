# Original problem: https://www.hackerrank.com/challenges/find-angle/problem
if __name__ == '__main__':
    import math

    AB = int(input())
    BC = int(input())
    print(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')
