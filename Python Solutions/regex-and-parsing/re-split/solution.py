# Original problem: https://www.hackerrank.com/challenges/re-split/problem
if __name__ == '__main__':
    import re

    regex_pattern = r'(?<=\d)[.,](?=\d)'
    print("\n".join(re.split(regex_pattern, input())))
``