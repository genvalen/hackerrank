# Original problem: https://www.hackerrank.com/challenges/merge-the-tools/problem
from collections import OrderedDict

def merge_the_tools(s, k):
    '''Create substrings of length k from s, and return unique letters in order of appearance.'''
    for i in range(0, len(s), k):
        sub = s[i:i+k]
        print("".join(OrderedDict().fromkeys(sub)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)