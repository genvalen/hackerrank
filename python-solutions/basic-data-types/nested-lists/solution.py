#Original problem: https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)

    lowest = min(scores)
    for i in range(scores.count(lowest)):
        scores.remove(lowest)

    students.sort()

    for i in students:
        if i[1] == min(scores):
            print(i[0])