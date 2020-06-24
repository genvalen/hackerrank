# Original problem: https://www.hackerrank.com/challenges/python-time-delta/problem
from datetime import datetime
import os

def get_datetime(time):
    "convert string to datetime object"
    return datetime.strptime(time, "%a %d %b %Y %X %z")


def time_delta(t1, t2):
    d1 = get_datetime(t1)
    d2 = get_datetime(t2)
    return(str(abs(int((d1-d2).total_seconds()))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()
    