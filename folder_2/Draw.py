import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

def draw_rectangles(rectangles):
    # Create a rectangle object with width=120 and height=100
    rect = Rectangle((0, 0), 125, 105)

    # Create a figure and axes object
    fig, ax = plt.subplots()




    # Add the rectangle to the axes
    ax.add_patch(rect)

    for rectangle in rectangles:
        
        verts = rectangle.verts
        
        rectangle_polygon = Polygon(verts, fill=False)
        ax.add_patch(rectangle_polygon)
        
    # Set the limits of the axes

    rect_1 = Rectangle((2.5, 2.5), 120, 100, linewidth=2, edgecolor='red', facecolor='none')

    ax.add_patch(rect_1)

    ax.set_xlim(0, 125)
    ax.set_ylim(0, 105)

    # Display the plot
    #plt.show()
    #if (index == 9999):
    plt.savefig("./folder_2/images/test.png", dpi=300)
    ##plt.savefig("./images/" + str(index) + 'hexagon' + str(hex_width) + str(hex_height) + str(hex_side) + rotation + '.png', dpi=300)

    plt.close()