class hero :
    def __init__(self,widthHero, heightHero ):
        self.x = mouseX  # x-coordinate
        self.y = mouseY  # y-coordinate
        self.widthHero = widthHero  # Left and right angle offset
        self.heightHero = heightHero  # Used to define the tilt
        self.top = self.y 
        self.botom = self.y + self.heightHero
        self.left = self.x
        self.right = self.x + self.widthHero
        
    def update(self):
        
        self.x = mouseX  # x-coordinate
        self.y = mouseY  # y-coordinate
        self.top = self.y 
        self.botom = self.y + self.heightHero
        self.left = self.x
        self.right = self.x + self.widthHero
        
        rect(mouseX,mouseY,self.widthHero, self.heightHero)