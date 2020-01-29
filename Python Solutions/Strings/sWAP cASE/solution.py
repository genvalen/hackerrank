# Original problem: https://www.hackerrank.com/challenges/swap-case/problem
# alternate to s.swapcase()
def swap_case(s):
    new_s = [i.lower() if i.isupper() else i.upper() if i.islower() else i for i in s]
    return ("").join(new_s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)