#Original problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    max_val = max(arr)
    while max(arr) == max_val:
        arr.remove(max(arr))
    print(max(arr))