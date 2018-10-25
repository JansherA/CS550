
from PIL import Image, ImageDraw
import random
fractal_level = 3
colblue = (0,61,103)
colbk = (0,0,0)

def fract_draw(x, y, width, height, count):
    color = random.sample(xrange(0,255), 3)
    pygame.draw.line(screen,color,[x + width*.25,height//2+y],[x + width*.75,height//2+y],2)
    color = random.sample(xrange(0,255), 3)
    pygame.draw.line(screen,color,[x+width*.25,(height*.5)//2+y],[x+width*.25,(height*1.5)//2+y],2)
    color = random.sample(xrange(0,255), 3)
    pygame.draw.line(screen,color,[x + width*.75,(height*.5)//2+y],[x + width*.75,(height*1.5)//2+y],2)
    
fract_draw(x, y, width, height, count)
