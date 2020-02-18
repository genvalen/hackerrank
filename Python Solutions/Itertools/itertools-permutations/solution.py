# Original problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
if __name__ == '__main__':
    from itertools import permutations

    s, k = input().split()
    [print("".join(i)) for i in sorted(permutations(list(s), int(k)))]
