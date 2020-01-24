#Original problem: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

if __name__=='__main__':
    year = int(input())
    print(is_leap(year))