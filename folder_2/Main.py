from folder_2 import Draw as d 
from folder_2 import Rectangle as r
import csv

rect_height = 105
rect_width = 125


def place_rect(L, l):
    """
    Place rectangles on a grid of dimensions L x l and return a list of Rectangle objects.

    Args:
    L (float): Width of the rectangle.
    l (float): Height of the rectangle.

    Returns:
    rectangles (list): List of Rectangle objects with given dimensions and placed on a grid.

    """
    origin = [L/2, l/2]
    rectangles = []
    
    while True:
        origin[0] = L/2

        while True:
            rectangles.append(r.Rectangle(L, l, origin[0], origin[1]))
            if origin[0] + L + L/2 + 0.2> rect_width:
                break
            else:
                origin[0] += L + 0.2
        if origin[1] + l + l/2 + 0.2 > rect_height:
            break
        else:
            origin[1] += l + 0.2

    last_origin = (rectangles[-1].center_x, rectangles[-1].center_y)

    slack_y = rect_height - last_origin[1] - l/2
    slack_x = rect_width - last_origin[0] - L/2

    for rectangle in rectangles:
        rectangle.update_points(slack_x/2, slack_y/2)

    return rectangles


def main(L, l):
    """
    Place rectangles of dimensions L x l and l x L on a grid and save the coordinates and rotation information
    of the rectangles in a CSV file. Draw the rectangles using the Draw class.

    Args:
    L (float): Width of the rectangle.
    l (float): Height of the rectangle.

    Returns:
    rectangles (list): List of Rectangle objects with given dimensions and placed on a grid.
    """
    rectangles_norot = place_rect(L, l)
    rectangles_rot = place_rect(l, L)

    if(len(rectangles_norot) > len(rectangles_rot)):
        rectangles = rectangles_norot
        save_on_csv(rectangles, 'no')
    else:
        rectangles = rectangles_rot
        save_on_csv(rectangles, 'yes')

    d.draw_rectangles(rectangles)

    return rectangles


def save_on_csv(rectangles, rotation):
    """
    Save the center coordinates and rotation information of the given rectangles in a CSV file.

    Args:
    rectangles (list): List of Rectangle objects to be saved in a CSV file.
    rotation (str): String specifying if the rectangles have been rotated or not.

    Returns:
    None
    """
    with open('rectangles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['x', 'y', 'rotazione'])

        for rectangle in rectangles:
            writer.writerow([rectangle.center_x, rectangle.center_y, rotation])