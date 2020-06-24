# Original problem: https://www.hackerrank.com/challenges/maximize-it/problem
if __name__=='__main__':
    from itertools import product
    k, m = map(int, input().split())

    lists = []
    for i in range(k):
        new_list = list(map(int, input().split()))
        lists.append(new_list[1:])

    total_sums = []
    for i in list(product(*lists)):
        pow_sum_mod_applied = sum(pow(element, 2) for element in i) % m
        total_sums.append(pow_sum_mod_applied) 
        
    print(max(total_sums))
    