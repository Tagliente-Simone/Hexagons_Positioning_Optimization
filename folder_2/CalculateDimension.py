from folder_2 import Main as m

def calculate_rectangle_dimensions(radius, short_side, long_side, rows, weight):
    """
    Calculates the total number of tubes required to build a rectangle with the given parameters.

    Parameters:
    radius (float): The radius of the tubes.
    short_side (float): The length of the shorter side of the rectangle.
    long_side (float): The length of the longer side of the rectangle.
    rows (int): The number of rows in the rectangle.

    Returns:
    int: The total number of tubes required.

    Raises:
    ValueError: If an unsupported number of rows is given.
    ValueError: If the calculated ratio is not within the acceptable range.
    """
    if int(rows) == 5:
        cost = 8.928
    elif int(rows) == 7:
        cost = 6.196 * 2
    elif int(rows) == 9:
        cost = 15.85
    else:
        raise ValueError("Unsupported number of rows")

    tube_length = radius * cost
    frame_width = radius * long_side * 2

    if tube_length < frame_width:
        ratio = frame_width / tube_length
    else:
        ratio = tube_length / frame_width

    if ratio < 1.12 or ratio > 1.14:
        raise ValueError("Invalid ratio")

    frame = m.main(frame_width, tube_length)
    return frame
    ##single_frame = (long_side * (int(int(rows) / 2)) + short_side * (int(rows) - int(int(rows) / 2)))
    ##print("single weight: " + str(weight) + " weight rect: " + str(weight * single_frame) + " of config " + str(rows) + "-" + str(rows-1))

    ##if single_frame * weight < 25:
    ##    total_tubes = len(frame) * single_frame
    ##    return total_tubes
    ##else:
    ##    return -1

    