#Original problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
if __name__ == '__main__':
    n, s = (input(), set(map(int, input().split())))

    for c in range(int(input())):
        try:
            cmd, *args = input().split()
            getattr(s, cmd) (*[int(x) for x in args])
        except: KeyError
        
    print(sum(s))
    