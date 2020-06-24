# Original problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
cube = lambda x: x ** 3 

def fibonacci(n):
    """Return list containing first n numbers of fib. sequence."""
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib = [0, 1]
        for _ in range(n-2):
            fib.append(fib[-1] + fib[-2])
        return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    