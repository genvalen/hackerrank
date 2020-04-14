# Original problem: https://www.hackerrank.com/challenges/hex-color-code/problem
if __name__ == '__main__':
    import re

    n = int(input())
    pattern = re.compile(r'.(#[\da-fA-F]{6}|#[\da-fA-F]{3})')

    for _ in range(n):
        m = re.findall(pattern, input())
        if m:
            print(*m, sep = '\n')
