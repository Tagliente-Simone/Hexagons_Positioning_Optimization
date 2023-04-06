import math
import Main as m

## Calculate the dimension of the hexagon

def Calculate(radius, n_rows, rows_array, index):

    B_min = 2 * radius * (max(rows_array) - 1)
    b_min = 2 * radius * (min(rows_array) - 1)
    obl_min = int(n_rows / 2) * radius * 2

    temp = (B_min - b_min) / 2

    h_min = math.sqrt(obl_min ** 2 - temp ** 2)

    h_max = h_min + radius

    k = h_max / h_min

    B_max = B_min * k
    b_max = b_min * k



    return m.compute(B_max, h_max * 2, b_max, index)
