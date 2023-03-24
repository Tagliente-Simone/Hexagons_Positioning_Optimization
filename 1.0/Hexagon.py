## This class represents a hexagon object with its origin and its vertices (6 points).
# The vertices are stored in a list of tuples. The vertices are ordered in a clockwise manner.
class Hexagon:


    ## Constructor
    def __init__(self, origin_x, origin_y, hex_width, hex_height, vertical_side_length):
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

    ## Rotate the hexagon 90 degrees
    def rotate90(self):
            self.verts = [(self.origin_y, self.origin_x - self.hex_width/2),
                            (self.origin_y + self.hex_height/2, self.origin_x - self.vertical_side_length/2),
                            (self.origin_y + self.hex_height/2, self.origin_x + self.vertical_side_length/2),
                            (self.origin_y, self.origin_x + self.hex_width/2),
                            (self.origin_y - self.hex_height/2, self.origin_x + self.vertical_side_length/2),
                            (self.origin_y - self.hex_height/2, self.origin_x - self.vertical_side_length/2)
                            ]
        
    

    ## Traslate the hexagon by a given slack
    def update_points(self, slack_x, slack_y):
        for i in range(len(self.verts)):
            self.verts[i] = (self.verts[i][0] + slack_x, self.verts[i][1] + slack_y)

