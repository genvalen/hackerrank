# Original problem: https://www.hackerrank.com/challenges/np-dot-and-cross/problem
if __name__ == '__main__':
    import numpy
    n = int(input())

    a = [list(map(int, input().split())) for i in range(n)]
    b = [list(map(int, input().split())) for i in range(n)]

    # Matrix multiplication is dot multiplication
    print(numpy.dot(a,b))
    