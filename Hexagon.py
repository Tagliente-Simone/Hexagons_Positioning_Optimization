class Hexagon:
    def __init__(self, origin_x, origin_y, hex_width, hex_height):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.hex_width = hex_width
        self.hex_height = hex_height
        self.x1 = self.origin_x - self.hex_width/2
        self.y1 = self.origin_y
        self.x2 = self.origin_x - self.hex_width/4
        self.y2 = self.origin_y - self.hex_height/2
        self.x3 = self.origin_x + self.hex_width/4
        self.y3 = self.origin_y - self.hex_height/2
        self.x4 = self.origin_x + self.hex_width/2
        self.y4 = self.origin_y
        self.x5 = self.origin_x + self.hex_width/4
        self.y5 = self.origin_y + self.hex_height/2
        self.x6 = self.origin_x - self.hex_width/4
        self.y6 = self.origin_y + self.hex_height/2

    
    def rotate90(self):
        self.x1, self.y1 = self.y1, self.x1
        self.x2, self.y2 = self.y2, self.x2
        self.x3, self.y3 = self.y3, self.x3
        self.x4, self.y4 = self.y4, self.x4
        self.x5, self.y5 = self.y5, self.x5
        self.x6, self.y6 = self.y6, self.x6

        

