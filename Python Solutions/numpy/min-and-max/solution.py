# original problem: https://www.hackerrank.com/challenges/np-min-and-max/problem
if __name__ == '__main__':
    import numpy as np 

    n, m = map(int,input().split())
    ar = [(list(map(int, input().split()))) for i in range(n)]
    np_ar = np.array(ar)

    #isolates row containing min value 
    min_val = np.min(np_ar, axis = 1)

    # isolates column containing max value
    max_val = np.max(min_val, axis = 0)

    print(max_val)
    