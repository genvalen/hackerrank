# Original problem: https://www.hackerrank.com/challenges/collections-counter/problem
if __name__ == '__main__':
    from collections import Counter

    shoes = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    customers = int(input())
    profit = 0

    for i in range(customers):
        size, price = list(map(int, input().split()))
        if shoe_sizes[size]:
            profit += price
            shoe_sizes[size] -= 1

    print(profit)