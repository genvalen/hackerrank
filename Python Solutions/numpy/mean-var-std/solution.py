# original problem: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
if __name__ == '__main__':
    import numpy as np

    n, m = map(int, input().split())
    ar =[list(map(int, input().split())) for i in range(n)]

    # legacy param tells np to print format setting for np ver. 1.13, 
    # instead of current ver. 1.14.
    np.set_printoptions(legacy = '1.13')

    print(np.mean(ar, axis = 1), np.var(ar, axis = 0), np.std(ar), sep= "\n")
