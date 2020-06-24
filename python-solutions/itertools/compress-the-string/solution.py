# Original problem: https://www.hackerrank.com/challenges/compress-the-string/problem
if __name__ == '__main__':
    from itertools import groupby

    s = input()
    for k, v in groupby(s):
        print((len(list(v)), int(k)), end = " ")
