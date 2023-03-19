import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
import Hexagon as hx
import numpy as np

def rotate_point(point):
    x, y = point
    return (-y, x)



def draw_rectangle(hexagons, rotate):
    # Create a rectangle object with width=120 and height=100
    rect = Rectangle((0, 0), 120, 100)

    # Create a figure and axes object
    fig, ax = plt.subplots()

    # Add the rectangle to the axes
    ax.add_patch(rect)

    for hexagon in hexagons:
        #calculate the vertex 
        x1, y1 = hexagon.x1, hexagon.y1
        x2, y2 = hexagon.x2, hexagon.y2
        x3, y3 = hexagon.x3, hexagon.y3
        x4, y4 = hexagon.x4, hexagon.y4
        x5, y5 = hexagon.x5, hexagon.y5
        x6, y6 = hexagon.x6, hexagon.y6

        verts = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6)]

        if rotate:
            verts_centered = [(x - hexagon.origin_x, y - hexagon.origin_y) for x, y in verts]
            rot_matrix = np.array([[0, -1], [1, 0]])
            verts_rotated = [rot_matrix.dot(np.array([x, y])) for x, y in verts_centered]
            verts_rotated_centered = [(x + hexagon.origin_x, y + hexagon.origin_y) for x, y in verts_rotated]
            hexagon = Polygon(verts_rotated_centered, fill=False)
        
        else:
            
            hexagon = Polygon(verts, fill=False)

        ax.add_patch(hexagon)

    # Set the limits of the axes
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 100)

    # Display the plot
    plt.show()