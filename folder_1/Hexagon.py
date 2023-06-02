## This class represents a hexagon object with its origin and its vertices (6 points).
# The vertices are stored in a list of tuples. The vertices are ordered in a clockwise manner.
class Hexagon:

    ## Constructor
    def __init__(self, origin_x, origin_y, hex_width, hex_height, vertical_side_length):
        """
        Initializes a new instance of the Hexagon class.

        Args:
        - origin_x (float): The x-coordinate of the hexagon's origin.
        - origin_y (float): The y-coordinate of the hexagon's origin.
        - hex_width (float): The width of the hexagon.
        - hex_height (float): The height of the hexagon.
        - vertical_side_length (float): The length of the vertical sides of the hexagon.

        Returns:
        A new instance of the Hexagon class.
        """
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.hex_width = hex_width
        self.hex_height = hex_height
        self.vertical_side_length = vertical_side_length
        self.verts = [(self.origin_x - self.hex_width/2, self.origin_y),
                      (self.origin_x - self.vertical_side_length/2, self.origin_y - self.hex_height/2),
                      (self.origin_x + self.vertical_side_length/2, self.origin_y - self.hex_height/2),
                      (self.origin_x + self.hex_width/2, self.origin_y),
                      (self.origin_x + self.vertical_side_length/2, self.origin_y + self.hex_height/2),
                      (self.origin_x - self.vertical_side_length/2, self.origin_y + self.hex_height/2)
                      ]

    ## Traslate the hexagon by a given slack
    def update_points(self, slack_x, slack_y):
        """
        Translates the hexagon by a given slack in the x and y directions.

        Args:
        - slack_x (float): The amount to translate the hexagon in the x direction.
        - slack_y (float): The amount to translate the hexagon in the y direction.

        Returns:
        None.
        """
        for i in range(len(self.verts)):
            self.verts[i] = (self.verts[i][0] + slack_x, self.verts[i][1] + slack_y)



