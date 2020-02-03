#Original problem: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    items = set(array)
    avg = sum(items)/ len(items)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)