class ball :
    def __init__(self, size, startX, startY):
        self.xBall = startX  # x-coordinate
        self.yBall = startY  # y-coordinate
        self.diametre = size  # Left and right angle offset
        self.xdirection = 1
        self.ydirection = 1
        self.counter = 0

    def update(self, heroWidth, heroHeight ):
        xspeed = 5.8  #Speed of the shape
        yspeed = 10.2  #Speed of the shape
        print("B is at " + str(self.yBall))
        print("hero is at " + str(mouseY-(self.diametre/2)) + " and " + str(mouseY+(self.diametre/2)+heroHeight) )
        
        if (self.yBall > mouseY-(self.diametre/2) and self.yBall < mouseY+(self.diametre/2)+heroHeight and self.xBall > mouseX and self.xBall < mouseX + heroWidth) :
            
            print("#######")   
            print("paddle")
            print("#######")
            if self.ydirection == 1 and self.yBall + ( yspeed * self.ydirection )> mouseY -(self.diametre/2) :
                self.counter = 1
                print("Too close from top")
            if self.ydirection == -1 and self.yBall + ( yspeed * self.ydirection )< mouseY+(self.diametre/2)+heroHeight  :
                self.counter = -1
                print("Too close from bottom")
            
            self.ydirection *= -1
            yspeed *=2
            
        if (self.xBall > width-self.diametre or self.xBall < self.diametre) :
            self.xdirection *= -1
            yspeed *= 3
            print("Xwall")
            
        if (self.yBall > height-self.diametre or self.yBall < self.diametre ) :
            self.ydirection *= -1
            yspeed *= 3
            print("Ywall")
            
        
                    
        self.xBall = self.xBall + ( xspeed * self.xdirection )
        if (self.counter == 1 or self.counter == -1 ) :
            if self.counter == 1 :
                self.yBall = mouseY -(self.diametre/2)
                print("you are on top at " + str(self.yBall))
                print("as shown by mouseY " + str(mouseY -(self.diametre/2)))
    
                self.counter = 0
            else :
                self.yBall = mouseY+(self.diametre/2)+heroHeight
                self.counter = 0
                print("you are at the bottom at " + str(self.yBall))
                print("as shown by mouseY +heroheight " + str((mouseY+(self.diametre/2)+heroHeight)))
        else :
            self.yBall = self.yBall + ( yspeed * self.ydirection )
            
        if self.ydirection == 1 :
            print("coming from the top")
        else :
            print("coming from the bottom")
        ellipse(self.xBall,self.yBall,self.diametre, self.diametre)
        print("B is now at " + str(self.yBall))
        print("hero is now at " + str(mouseY-(self.diametre/2)) + " and " + str(mouseY+(self.diametre/2)+heroHeight) )