from hero import hero
from ball import ball

def setup():
    size(500, 500)
    global h1
    global b1

    background (255)
    h1 = hero(50, 10)
    b1 = ball(25,67,32)

    frameRate(30);
    
def draw():
    background (255)
    h1.update()
    b1.update()
    
    #walls
    
    if b1.left <= 0 or b1.right >= width :
        b1.changeCourse('x')
    if b1.top <= 0 or b1.bottom >= height :
        b1.changeCourse('y')
        
    #hero

    if ((b1.left <= h1.right and b1.right>= h1.left) and (b1.bottom > h1.top - b1.yspeed) and (b1.bottom < h1.top + b1.yspeed)):
        b1.changeCourse('y')
   # if ((b1.left <= h1.right and b1.right>= h1.left) and (b1.top > h1.bottom + b1.yspeed) and (b1.top < h1.top + b1.yspeed)):
     #   b1.changeCourse('y')
    
        
   # if b1.top <= 0 or b1.bottom >= height :
   #     b1.changeCourse('y')
    

    