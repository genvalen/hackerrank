# Original problem: https://www.hackerrank.com/challenges/np-polynomials/problem
if __name__ == '__main__':
    import numpy as np
    coef = list(map(float, input().split()))
    x = int(input())

    print(np.polyval(coef, x))
