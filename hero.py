class hero :
    def __init__(self):
        self.xHero = 0  # x-coordinate
        self.yHero = 0  # y-coordinate
        self.widthHero = 50  # Left and right angle offset
        self.heightHero = 10  # Used to define the tilt
    def update(self,x,y):
        rect(x,y,self.widthHero, self.heightHero)