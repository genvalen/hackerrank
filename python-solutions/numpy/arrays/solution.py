# Original problem: https://www.hackerrank.com/challenges/np-arrays/problem
def arrays(arr):
    return numpy.array(arr[::-1],float)
   
if __name__ == '__main__':
    import numpy

    arr = input().strip().split(' ')