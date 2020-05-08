if __name__ == '__main__':
    import numpy

    n, m = map(int, input().split())
    arr = str(numpy.eye(n, m, k = 0))
    
    print(arr.replace('1', ' 1').replace('0', ' 0'))
