from polyomino import *
from utils import *

def algorithm(matrix, solution):
    if not matrix.size:
        return True
    transp = matrix.T
    rows = set(i for i in range(matrix.shape[0]))
    cols = set(i for i in range(matrix.shape[1]))
    if not cols:
        return False
    min = 1000000000
    n_min = 0
    for col in cols:
        count = np.count_nonzero(transp[col] == 1)
        if count < min and count > 0:
            min = count
            n_min = col
    c = n_min
    if np.sum(matrix[:, c]) == 0:
        return False
    tmp = matrix
    for i in range(matrix[:, c].size):
        solution.append(matrix[i])
        for j in range(matrix[i].size):
            if matrix[i, j] == 1:
                for k in range(matrix[:, c].size):
                    if matrix[k, j] == 1:
                        tmp = np.delete(matrix, k, 0)
                tmp = np.delete(tmp, j, 1)
    matrix = tmp
    return algorithm(matrix, solution)

def main(table_shape, r_input, l_input):

    r = [RPolyomino(r[0]) for r in r_input for i in range(r[1])]
    l = [LPolyomino(l[0]) for l in l_input for i in range(l[1])]

    if not check_area(table_shape, r_input, l_input):
        return False
    if not check_length(table_shape, r_input, l_input):
        return False

    table = [[(i, j) for j in range(table_shape[0])] for i in range(table_shape[1])]

    for el in r:
        el.set_positions(table, el.width == el.height)

    for el in l:
        el.set_positions(table)

    matrix = get_matrix(table, r, l)
    solution = []

    return algorithm(matrix, solution)

if __name__ == '__main__':
    #для запуска программы:
    # 1. поменять значения входных параметров (table_shape, r_input, l_input)
    # 2. запустить main.py в любой удобной среде, поддерживающей python 3 (код написан в PyCharm)
    table_shape = (4, 4)
    r_input = [((1, 1), 1)]
    l_input = [((4, 4), 2)]

    if main(table_shape, r_input, l_input):
        print("Правда")
    else:
        print("Ложь")
