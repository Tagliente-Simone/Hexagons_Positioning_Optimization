import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
import numpy as np

def draw_rectangles(rectangles):
    # Create a rectangle object with width=120 and height=100
    rect = Rectangle((0, 0), 124, 104, facecolor='blue', edgecolor='black', linewidth=2)
    


    # Create a figure and axes object
    fig, ax = plt.subplots()
    
    # Add the rectangle to the axes
    ax.add_patch(rect)

    # Set the limits of the axes

    rect_1 = Rectangle((2, 2), 120, 100, linewidth=1, facecolor='green')

    ax.add_patch(rect_1)




    for rectangle in rectangles:
        
        verts = rectangle.verts
        
        rectangle_polygon = Polygon(verts, fill=True, facecolor='#D3D3D3', edgecolor='black', linewidth=0.5)
        ax.add_patch(rectangle_polygon)
        # Plotting the dot
        plt.scatter(rectangle.center_x, rectangle.center_y, color='black', marker='x')
        
        


    ax.set_xlim(0, 125)
    ax.set_ylim(0, 105)
    
    axis = plt.gca()
    
    # Set the desired step length for the x-axis
    step = 5

    # Generate new tick positions based on the step length for the x-axis
    new_xticks = np.arange(0, 125, step)
    new_yticks = np.arange(0, 105, step)
    

    # Set the new tick positions
    axis.set_xticks(new_xticks)
    axis.set_yticks(new_yticks)
    
    # Decrease the font size of x-axis labels
    axis.set_xticklabels(axis.get_xticklabels(), fontsize=5)

    # Decrease the font size of y-axis labels
    axis.set_yticklabels(axis.get_yticklabels(), fontsize=5)


    
    # Set the aspect ratio to 'equal'
    ax.set_aspect('equal')
    
    

    #plt.axis('off')
    # Display the plot
    #plt.show()
    #if (index == 9999):
    plt.savefig("./images/rect.png", dpi=300)
    ##plt.savefig("./images/" + str(index) + 'hexagon' + str(hex_width) + str(hex_height) + str(hex_side) + rotation + '.png', dpi=300)

    plt.close()