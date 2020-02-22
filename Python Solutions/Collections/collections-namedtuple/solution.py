# Original problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
if __name__ == '__main__':
    from collections import namedtuple

    n = int(input())
    columns = input()
    Student = namedtuple('Student', columns)

    marks = 0
    for i in range(n):
        marks += int(Student._make(input().split()).MARKS)

    print("{:.2f}".format(marks/n))
