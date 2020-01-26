#Original problem: https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = (int(input()))
    command = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
    ar = []
    for i in range (N):
        value = input().split()
        if value[0] == "insert":
            ar.insert(int(value[1]), int(value[2]))
        elif value[0] == "print":
            print(ar) 
        elif value[0] == "remove":
            ar.remove(int(value[1]))
        elif value[0] == "append":
            ar.append(int(value[1]))
        elif value[0] == "sort":
            ar.sort()
        elif value[0] == "pop":
            ar.pop()
        elif value[0] == "reverse":
            ar.reverse()