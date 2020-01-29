# Original problem: https://www.hackerrank.com/challenges/string-validators/problem
if __name__ == '__main__':
    s = input()
    cmds = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    
    for c in cmds: 
        if any(eval('i.' + c + '()') for i in s):
            print(True)
        else:
            print(False)