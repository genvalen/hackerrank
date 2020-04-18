# Original problem: https://www.hackerrank.com/challenges/designer-door-mat/problem
N, M = map(int, input().split(" "))
welcome = "WELCOME"
line = ".|."
lines = []

for i in range(N//2):
    print (line.center(M, "-"))
    lines.append(line)
    line = ".|." + line + ".|."

print(welcome.center(M, "-"))

for j in range((N//2)-1,-1,-1):
    print(lines[j].center(M, "-"))