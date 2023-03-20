import math
import Main as m

def Calculate(radius, n_rows, rows_array):

    k = n_rows / 2
    B_min = 2 * radius * (max(rows_array) - 1)
    b_min = 2 * radius * (rows_array[0] - 1)
    h_min = k * radius * math.sqrt(3)

    B_max = B_min * (1 + 1/(k * math.sqrt(3)))
    b_max = b_min * (1 + 1/(k * math.sqrt(3)))
    h_max = h_min * (1 + 1/(k * math.sqrt(3)))

    m.compute(h_max * 2, B_max, b_max)

