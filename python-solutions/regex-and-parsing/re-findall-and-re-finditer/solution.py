# Orginal problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
if __name__ == '__main__':
    import re
    c = "qwrtypsdfghjklzxcvbnm"
    v = "aeiou"
    pattern = r"(?<=[%s])([%s]{2,})(?=[%s])" % (c, v, c)
    matches = re.findall(pattern, input(), re.IGNORECASE)

    [print(match) if matches else print(-1) for match in matches]