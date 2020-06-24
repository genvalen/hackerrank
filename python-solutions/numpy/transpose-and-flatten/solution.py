# Original problem: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
if __name__ == '__main__':
    import numpy as np
    
    n, m = list(map(int, input().split()))
    matrix = [[c for c in range(m)] for r in range(n)]

    array = np.array(matrix)

    print(np.transpose(array))
    print(array.flatten())
