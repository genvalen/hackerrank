# Original problem: https://www.hackerrank.com/challenges/zipped/problem
if __name__ == '__main__':
    n, x = map(float, input().split())

    scores = []
    for i in range(int(x)):
        scores.append(list(map(float, input().split())))

    for i in zip(*scores):
        print("{:0.1f}".format(sum(i)/x))