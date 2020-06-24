# Original problem: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
def repl(m):
    if m.group(0) == '&&':
        return 'and'
    else:
        return 'or'


if __name__ == '__main__':
    import re

    n = int(input())
    pattern = r'(?<=[ ])([&|])\1{1}(?=[ ])'

    for i in range(n):
        print(re.sub(pattern, repl, input()))
        