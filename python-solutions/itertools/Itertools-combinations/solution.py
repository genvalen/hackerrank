# Original problem: https://www.hackerrank.com/challenges/itertools-combinations/problem
if __name__ == '__main__':
    from itertools import combinations

    s, k = input().split()
    [print("".join(i)) for j in range(1, int(k)+1) for i in combinations(sorted(s), j)]
