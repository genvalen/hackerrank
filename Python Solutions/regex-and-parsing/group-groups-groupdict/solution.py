# Original problem: https://www.hackerrank.com/challenges/re-group-groups/problem
if __name__ == '__main__':
    import re

    s = input()
    pattern = re.compile(r'([a-zA-Z0-9])\1+')
    match = re.search(pattern, s)

    if match:
        print(match.group(1))
    else:
        print(-1)
