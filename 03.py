from PIL import Image, ImageDraw
import random
def triangle(n): 
  im = Image.new('RGB', (512,512), (0, 0, 0))
  y = n - 1
  while(y >= 0) : 
    i = 0
    while(i < y ): 
      i = i + 1 
    x = 0
    while(x + y < n ): 
      y = y - 1
      oh = random.randrange(0,255,1)
      hi = random.randrange(0,255,1)
      hello = random.randrange(0,255,1)
      if ((x & y) != 0) : 
        im.putpixel((x,y), (0,0,0)) 
      else : 
        x = x + 1
        im.putpixel((x,y), (oh,hi,hello)) 

  im.show()
n = 16
  
triangle(n) 



