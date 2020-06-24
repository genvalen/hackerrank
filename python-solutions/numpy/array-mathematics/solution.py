if __name__ == '__main__':
    import numpy

    n, m = map(int, input().split())

    # captures array of n dimensions, each iteration is an element
    a = numpy.array([input().split() for i in range(n)], int)
    b = numpy.array([input().split() for i in range(n)], int)

    # operations
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(a**b)
