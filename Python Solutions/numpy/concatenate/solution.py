# Original problem:
if __name__ == '__main__':
    import numpy as np

    n, m, p = map(int, input().strip().split())
    n_list = []
    m_list= []
        
    for i in range(n):
        n_list.append(list(map(int, input().split())))

    for j in range(m):
        m_list.append(list(map(int, input().split())))

    ar1 = np.array(n_list)
    ar2 = np.array(m_list)

    print(np.concatenate((ar1, ar2), axis = 0))
    