# Original problem: https://www.hackerrank.com/challenges/re-start-re-end/submissions/code/141459296
if __name__ == '__main__':
    import re

    s = input()
    k = input()

    pattern = re.compile(k)
    m = re.search(pattern, s)

    if not m: 
        print((-1, -1))
    while m:
        print('({}, {})'.format(m.start(), m.end()-1))
        m = pattern.search(s, m.start()+1)
