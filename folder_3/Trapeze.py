class Trapeze:
    
    def __init__(self, a, b, h, origin_x, origin_y):
        self.a = a
        self.b = b
        self.h = h
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.verts = [(self.origin_x - self.a/2, self.origin_y - self.h/2),
                        (self.origin_x + self.a/2, self.origin_y - self.h/2),
                        (self.origin_x + self.b/2, self.origin_y + self.h/2),
                        (self.origin_x - self.b/2, self.origin_y + self.h/2)]
        
        
        
    def update_points(self, slack_x, slack_y):
        
        self.origin_x += slack_x
        self.origin_y += slack_y
        
        self.verts = [(self.origin_x - self.a/2, self.origin_y - self.h/2),
                        (self.origin_x + self.a/2, self.origin_y - self.h/2),
                        (self.origin_x + self.b/2, self.origin_y + self.h/2),
                        (self.origin_x - self.b/2, self.origin_y + self.h/2)]
        
        