# Original problem: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
if __name__ == '__main__':
    import numpy as np

    shape = list(map(int, input().split()))

    print(np.zeros(shape, dtype = np.int))
    print(np.ones(shape, dtype = np.int))
    