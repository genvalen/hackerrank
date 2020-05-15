if __name__ == '__main__':
    import numpy as np

    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(n)]

    # sum and prod operations
    list_of_sums = np.sum(matrix, axis = 0)
    product = np.prod(list_of_sums)

    print(product)
