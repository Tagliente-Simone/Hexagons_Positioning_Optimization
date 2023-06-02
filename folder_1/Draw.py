import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon

def draw_hexagons(hexagons):
    # Create a rectangle object with width=120 and height=100
    rect = Rectangle((0, 0), 125, 105, facecolor='blue', edgecolor='black', linewidth=2)
    


    # Create a figure and axes object
    fig, ax = plt.subplots()
    
    # Add the rectangle to the axes
    ax.add_patch(rect)
    
    rect_1 = Rectangle((2.5, 2.5), 120, 100, linewidth=1, edgecolor='red', facecolor='green')

    ax.add_patch(rect_1)






    for hexagon in hexagons:
        verts = hexagon.verts
        
        hexagon_polygon = Polygon(verts, fill=True, facecolor='white', edgecolor='black', linewidth=1)
        ax.add_patch(hexagon_polygon)
        # Plotting the dot
        plt.scatter(hexagon.origin_x, hexagon.origin_y, color='black', marker='x')
        
        
    # Set the limits of the axes


    ax.set_xlim(0, 125)
    ax.set_ylim(0, 105)
    

    plt.axis('off')

    # Display the plot
    #plt.show()
    plt.savefig("./folder_1/images/hex.png", dpi=300)
    ##plt.savefig("./images/" + str(index) + 'hexagon' + str(hex_width) + str(hex_height) + str(hex_side) + rotation + '.png', dpi=300)

    plt.close()

