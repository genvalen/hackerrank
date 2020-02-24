# Original problem: https://www.hackerrank.com/challenges/most-commons/problem
# Counter information: https://docs.python.org/2/library/collections.html#collections.Counter
from collections import Counter

def logo_facilitator(string):
    for i in Counter(sorted(string)).most_common(3):
        print(*i)

if __name__ == '__main__':
    s = input()
    logo_facilitator(s)