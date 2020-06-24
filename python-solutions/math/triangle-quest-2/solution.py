# Original problem: https://www.hackerrank.com/challenges/triangle-quest-2/problem
if __name__ == '__main__':
    for i in range(1,int(input())+1): 
        print((10**i // 9)**2)

    # CONCEPT
    # 10**1 // 9 = 1
    # 10**2 // 9 = 11
    # 10**3 // 9 = 111

    # 1*1 = 1
    # 11*11 = 121
    # 111*111 = 12321
