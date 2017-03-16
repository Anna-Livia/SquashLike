from hero import hero
from ball import ball

def setup():
    size(640, 360)
    global h1
    global b1
    background (255)
    h1 = hero()
    b1 = ball()
    
def draw():
    background (255)
    h1.update(mouseX, mouseY)
    b1.update(mouseY, mouseX, h1.widthHero)
    