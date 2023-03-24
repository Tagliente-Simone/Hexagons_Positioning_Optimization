import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
import Hexagon as hx

def draw_rectangle(hexagons, hex_width, hex_height, hex_side, rotation, index):
    # Create a rectangle object with width=120 and height=100
    rect = Rectangle((0, 0), 120, 100)

    # Create a figure and axes object
    fig, ax = plt.subplots()

    # Add the rectangle to the axes
    ax.add_patch(rect)

    for hexagon in hexagons:
        verts = hexagon.verts
        
        hexagon_polygon = Polygon(verts, fill=False)
        ax.add_patch(hexagon_polygon)
        
    # Set the limits of the axes
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 100)

    # Display the plot
    ##plt.show()
    ##plt.savefig("./images/" + str(index) + 'hexagon' + str(hex_width) + str(hex_height) + str(hex_side) + rotation + '.png', dpi=300)