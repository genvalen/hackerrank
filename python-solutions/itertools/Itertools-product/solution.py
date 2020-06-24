# Original problem: https://www.hackerrank.com/challenges/itertools-product/problem
if __name__ == '__main__':
    from itertools import product

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*list(product(a, b)))
