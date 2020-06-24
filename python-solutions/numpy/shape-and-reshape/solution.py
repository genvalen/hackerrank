# Original problem: https://www.hackerrank.com/challenges/np-shape-reshape/problem
if __name__ == '__main__':
    import numpy as np

    n = list(map(int, input().split()))

    array = np.array(n)

    print(np.reshape(array, (3,3)))
