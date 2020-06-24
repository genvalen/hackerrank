# Original problem: https://www.hackerrank.com/challenges/polar-coordinates/problem
if __name__ == '__main__':
    import cmath

    complex_num = complex(input())
    r = abs(complex_num)
    p = cmath.phase(complex_num)
    print(r, p, sep = '\n')
  