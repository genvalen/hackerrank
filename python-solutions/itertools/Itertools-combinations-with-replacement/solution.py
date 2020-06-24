# Original problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
if __name__ == '__main__':
    from itertools import combinations_with_replacement

    s, k = input().split()
    [print("".join(i)) for i in combinations_with_replacement(sorted(s), int(k))]
