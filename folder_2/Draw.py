import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

def draw_rectangles(rectangles):
    # Create a rectangle object with width=120 and height=100
    rect = Rectangle((0, 0), 125, 105, facecolor='blue', edgecolor='black', linewidth=2)
    


    # Create a figure and axes object
    fig, ax = plt.subplots()
    
    # Add the rectangle to the axes
    ax.add_patch(rect)

    # Set the limits of the axes

    rect_1 = Rectangle((2.5, 2.5), 120, 100, linewidth=1, edgecolor='red', facecolor='green')

    ax.add_patch(rect_1)




    for rectangle in rectangles:
        
        verts = rectangle.verts
        
        rectangle_polygon = Polygon(verts, fill=True, facecolor='white', edgecolor='black', linewidth=1)
        ax.add_patch(rectangle_polygon)
        # Plotting the dot
        plt.scatter(rectangle.center_x, rectangle.center_y, color='black', marker='x')
        
        


    ax.set_xlim(0, 125)
    ax.set_ylim(0, 105)

    plt.axis('off')
    # Display the plot
    #plt.show()
    #if (index == 9999):
    plt.savefig("./folder_2/images/rect.png", dpi=300)
    ##plt.savefig("./images/" + str(index) + 'hexagon' + str(hex_width) + str(hex_height) + str(hex_side) + rotation + '.png', dpi=300)

    plt.close()