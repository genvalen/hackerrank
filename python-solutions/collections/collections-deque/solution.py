# Original problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
if __name__ == '__main__':
    from collections import deque
    
    d = deque()

    for i in range(int(input())):
        cmd, *args = input().split()
        getattr(d, cmd)(*args)
        
    print(*d)
