# Original problem: https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    l = list(s)
    l[position] = character
    return "".join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    