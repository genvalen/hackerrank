# Original problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
if __name__ == '__main__':
    from collections import OrderedDict

    n = int(input())
    d = OrderedDict()

    for i in range(n):
        merch = input().split()
        item_name = " ".join(merch[:-1])
        net_price = int(merch[-1])
        
        if item_name in d:
            d[item_name] += net_price
        else:
            d[item_name] = net_price
            
    for k, v in d.items():
        print(k, v)