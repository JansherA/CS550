
from PIL import Image
from timeit import default_timer as t
start = t()
import random
xmin, xmax = -0.156998049092, -0.149590664054
ymin, ymax = 0.087830637949,0.082645468422
# xmin, xmax = -2, 2
# ymin, ymax = -2, 2
iterations = 256
imgx = 1024
imgy = 1024
im = Image.new("RGB", (imgx, imgy))
c = complex(-0.7399999999999998, 0.2999999999999994)
# c = complex(random.random() * 2.0 - 1.0, random.random() - 0.1)
for y in range(imgy):
    zy = y * (ymax - ymin) / (imgy - 1)  + ymin
    for x in range(imgx):
        zx = x * (xmax - xmin) / (imgx - 1) + xmin
        z = complex(zx, zy)
        for i in range(iterations):
            if abs(z) > 2.0: 
                break 
            z = z**2 + c 
        if iterations == 255: #This if statement guarentees the color of the middle of the fractal (max iterations) to be whatever I choose
            r = 30
            g = 144
            b = 255
        else: 
	        r = (i*50)%256
	        g = i % 4 * 128
	        b = i % 16 * 64
        im.putpixel((x, y), (r,g,b))
im.show()
elapsed_time = t() - start
print("The program took", str(elapsed_time),"seconds to run.")