# Original problem: https://www.hackerrank.com/challenges/python-quest-1/problem
if __name__ == '__main__':
    # Smarandache Sequences
    for i in range(1,int(input())):
        print(i * (10 ** i - 1) // 9)
     