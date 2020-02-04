#Original problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s =  set(map(int, input().split()))
cmds = [input().split() for _ in range(int(input()))]

for c in cmds:
    try:
        if len(c)> 1:
            eval('s.{}({})'.format(c[0], c[1]))
        else:
            eval('s.{}()'.format(c[0]))
    except: KeyError
    
print(sum(s))