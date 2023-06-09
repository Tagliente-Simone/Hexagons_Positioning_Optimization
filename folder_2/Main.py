from folder_2 import Draw as d 
from folder_2 import Rectangle as r
import shared_variable as sv
import csv

rect_height = sv.rect_height
rect_width = sv.rect_width

inter = sv.inter

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
            if origin[0] + L + L/2 + inter > rect_width:
                break
            else:
                origin[0] += L + inter
        if origin[1] + l + l/2 + inter > rect_height:
            break
        else:
            origin[1] += l + inter

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
    else:
        rectangles = rectangles_rot
    
    return rectangles


