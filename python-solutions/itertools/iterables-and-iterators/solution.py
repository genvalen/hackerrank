# Original problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
if __name__ == '__main__':
    from itertools import combinations

    n = int(input())
    s = input().split(" ")
    k = int(input())

    #save all combinations
    combos = list(combinations(s, k))

    #sum of combos containing 'a' divided by total combos
    probablility = sum(1 for x in combos if 'a' in x) / len(combos)
    
    print(probablility)
