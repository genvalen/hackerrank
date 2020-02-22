# Original problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
if __name__ == '__main__':
    from collections import defaultdict

    n, m = map(int, input().split())
    a_words, b_words = [input() for _ in range(n)], [input() for _ in range(m)]

    # set default values of d 
    # to an empty list
    d = defaultdict(list)

    for i in range(n):
            d[a_words[i]].append(i+1)

    for i in range(m):
        if b_words[i] in d:
            print(*d[b_words[i]])
        else:
            print(-1)
