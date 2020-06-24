# Original problem: https://www.hackerrank.com/challenges/np-inner-and-outer/problem
if __name__ == '__main__':
    import numpy

    #set print settings to numpy ver. 1.13 settings, 
    # instead of current ver. 1.14 settings
    numpy.set_printoptions(legacy = '1.13')

    a, b = [numpy.array(input().split(), dtype = int) for i in range(2)]

    print(numpy.inner(a,b), numpy.outer(a,b), sep = "\n")
    