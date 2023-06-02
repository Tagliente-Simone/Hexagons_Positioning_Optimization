class Rectangle:
    """
    A class representing a rectangle with a given width, height, center_x, and center_y.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        center_x (float): The x-coordinate of the center of the rectangle.
        center_y (float): The y-coordinate of the center of the rectangle.
        verts (list): The four vertices of the rectangle as (x, y) coordinates.
    """

    def __init__(self, width, height, center_x, center_y):
        """
        Constructs a new rectangle with the given dimensions and center coordinates.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
            center_x (float): The x-coordinate of the center of the rectangle.
            center_y (float): The y-coordinate of the center of the rectangle.
        """
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y

        # The vertices of the rectangle
        self.verts = [(self.center_x - self.width/2, self.center_y - self.height/2),
                      (self.center_x + self.width/2, self.center_y - self.height/2),
                      (self.center_x + self.width/2, self.center_y + self.height/2),
                      (self.center_x - self.width/2, self.center_y + self.height/2)]

    def update_points(self, slack_x, slack_y):
        """
        Updates the vertices of the rectangle by adding slack to their x and y coordinates.

        Args:
            slack_x (float): The amount of slack to add to the x coordinates of the vertices.
            slack_y (float): The amount of slack to add to the y coordinates of the vertices.
        """
        self.center_x += slack_x
        self.center_y += slack_y
        for i in range(len(self.verts)):
            self.verts[i] = (self.verts[i][0] + slack_x, self.verts[i][1] + slack_y)

            

    def rotate90(self):
        """
        Rotates the rectangle by 90 degrees by swapping its width and height and updating its vertices.
        """
        self.width, self.height = self.height, self.width
        self.verts = [(self.center_y - self.height/2, self.center_x - self.width/2),
                      (self.center_y - self.height/2, self.center_x + self.width/2),
                      (self.center_y + self.height/2, self.center_x + self.width/2),
                      (self.center_y + self.height/2, self.center_x - self.width/2)]


