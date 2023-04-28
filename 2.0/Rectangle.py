class Rectangle:
    def __init__(self, width, height, center_x, center_y):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.verts = [(self.center_x - self.width/2, self.center_y - self.height/2),
                        (self.center_x + self.width/2, self.center_y - self.height/2),
                        (self.center_x + self.width/2, self.center_y + self.height/2),
                        (self.center_x - self.width/2, self.center_y + self.height/2)
                        ]
        
    def update_points(self, slack_x, slack_y):
        for i in range(len(self.verts)):
            self.verts[i] = (self.verts[i][0] + slack_x, self.verts[i][1] + slack_y)

    
    def rotate90(self):
        self.verts = [(self.center_y - self.height/2, self.center_x - self.width/2),
                        (self.center_y - self.height/2, self.center_x + self.width/2),
                        (self.center_y + self.height/2, self.center_x + self.width/2),
                        (self.center_y + self.height/2, self.center_x - self.width/2)
                        ]

