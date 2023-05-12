import math
from folder_1 import Main as m

def calculate_hexagon_dimensions(radius, n_rows, rows_array, index):
    """
    Calculates the dimensions of a hexagonal shape based on the input parameters.

    Args:
        radius (float): The radius of the hexagon.
        n_rows (int): The number of rows in the hexagon.
        rows_array (list[int]): An array of integers representing the rows in the hexagon.
        index (int): An index used by the `m.compute` function.

    Returns:
        int: The total number of tubes in the hexagon.

    Raises:
        None.

    """
    # Calculate the minimum width of the hexagon
    B_min = 2 * radius * (max(rows_array) - 1)
    b_min = 2 * radius * (min(rows_array) - 1)
    obl_min = int(n_rows / 2) * radius * 2
    temp = (B_min - b_min) / 2
    h_min = math.sqrt(obl_min ** 2 - temp ** 2)

    # Calculate the maximum width of the hexagon
    h_max = h_min + radius
    k = h_max / h_min
    B_max = B_min * k
    b_max = b_min * k

    # Compute the total number of tubes in the hexagon
    total_tubes = m.compute(B_max, h_max * 2, b_max, index)

    return total_tubes
