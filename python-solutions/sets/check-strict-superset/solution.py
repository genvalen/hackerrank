# Original problem: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
if __name__ == '__main__':
    a = set(input().split())
    cases = []

    for i in range(int(input())):
        b = set(input().split())
        cases.append(a.issuperset(b))
        
    print(all(cases))
    