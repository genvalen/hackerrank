# Original problem: https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
if __name__ == '__main__':
    a, b, c, d = (int(input()) for _ in range(4))
    print(a ** b + c ** d)
    