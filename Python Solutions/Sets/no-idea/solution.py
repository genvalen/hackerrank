# Original problem: https://www.hackerrank.com/challenges/no-idea/problem
def hap_calc(arr, a, b):
    '''return happiness rate of arr based on elements in a and b.'''
    print(sum([(i in a) - (i in b) for i in arr]))

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    hap_calc(arr, a, b)
