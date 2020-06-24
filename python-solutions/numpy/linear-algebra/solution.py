if __name__ == '__main__':
    import numpy

    n = int(input())
    a = [list(map(float, input().split())) for i in range(n)]

    numpy.set_printoptions(legacy = "1.13")
    print(numpy.linalg.det(a))
