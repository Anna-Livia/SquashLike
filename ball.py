class ball :
    def __init__(self, diam, startX, startY):
        self.x  = startX  # x-coordinate
        self.y  = startY  # y-coordinate
        self.diametre = diam  # Left and right angle offset
        self.rad = diam/2
        self.top = startY - diam/2
        self.bottom = startY + diam/2
        self.left = startX - diam/2
        self.right = startY + diam/2
        self.xdirection = 1
        self.ydirection = 1
        self.counter = 0
        self.xspeed = 5.8
        self.yspeed = 10.2

    def update(self):
        self.x  = self.x  + ( self.xspeed * self.xdirection )
        self.y  = self.y  + ( self.yspeed * self.ydirection )
        self.top = self.y  - self.rad
        self.bottom = self.y  + self.rad
        self.left = self.x  - self.rad
        self.right = self.x  + self.rad
        
        ellipse(self.x ,self.y ,self.diametre, self.diametre)
        
    def changeCourse(self,variable) :

        if variable == "x" :
            self.xdirection *= -1
            
        else :
            self.ydirection *= -1

            
            
        