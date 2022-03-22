import numpy as np

def rotate(table):
    width = len(table[0])
    height = len(table)
    result = []
    for col in range(width):
        new_row = []
        for row in range(height):
            new_row.append(table[height - row - 1][col])
        result.append(new_row)
    return result

def reflect(table):
    return table[::-1]

def get_matrix(table, r, l):
    all_pos = []
    all_figs = r + l
    table_cells = []
    for row in table:
        table_cells += [cell for cell in row]
    for fig in all_figs:
        all_pos += fig.positions
    matr_1 = []
    for fig in all_figs:
        matr_1.append(list(map(lambda x: int(x in fig.positions), all_pos)))
    matr_2 = []
    for fig in all_figs:
        for pos in fig.positions:
            matr_2.append(list(map(lambda x: int(x in [i[j] for i in pos for j in range(len(i))]), table_cells)))
    matr_1 = np.array(matr_1).T
    matr_2 = np.array(matr_2)
    return np.concatenate((matr_1, matr_2), axis=1)

def check_area(table_shape, r_input, l_input):
    table_area = table_shape[0] * table_shape[1]
    r_area = sum([el[0][0] * el[0][1] * el[1] for el in r_input])
    l_area = sum([((el[0][0] + el[0][1]) - 1) * el[1] for el in l_input])
    return table_area >= r_area + l_area

def check_length(table_shape, r_input, l_input):
    table_max = max(table_shape)
    r_l_max = max([el[0][i] for el in r_input + l_input for i in range(len(el[0]))])
    return r_l_max <= table_max
