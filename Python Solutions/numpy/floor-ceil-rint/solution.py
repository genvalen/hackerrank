# original problem: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
if __name__ == '__main__':
    import numpy as np

    np.set_printoptions(sign=' ')

    array = np.array(list(map(float, input().split())))

    print(np.floor(array))
    print(np.ceil(array))
    print(np.rint(array))
