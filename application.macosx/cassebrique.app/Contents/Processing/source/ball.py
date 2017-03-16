class ball :
    def __init__(self):
        self.xBall = 15  # x-coordinate
        self.yBall = 15  # y-coordinate
        self.diametre = 10  # Left and right angle offset
        self.xdirection = 1
        self.ydirection = 1

    def update(self, heroY, heroX, heroWidth ):
        xspeed = 2.8  #Speed of the shape
        yspeed = 2.2  #Speed of the shape
        
        if (self.yBall > heroY-self.diametre and self.xBall > heroX and self.xBall < heroX + heroWidth) :
            self.ydirection *= -1
            
        if (self.xBall > width-self.diametre or self.xBall < self.diametre) :
            self.xdirection *= -1
            
        if (self.yBall > height-self.diametre or self.yBall < self.diametre ) :
            self.ydirection *= -1

        self.xBall = self.xBall + ( xspeed * self.xdirection )
        self.yBall = self.yBall + ( yspeed * self.ydirection )
        ellipse(self.xBall,self.yBall,self.diametre, self.diametre)