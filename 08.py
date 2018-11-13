#Mandlebrot and Julia's set fractal images
#Jansher Azmat
#No Sources
#Submitted Oct. 25
#Two Mandlebrot Images went smoothly and the transition to the Julia's set was quite easy
#On my honor, I have neither given nor received unauthorized aid

from PIL import Image
import random
# xmin, xmax = -1.5,0
# ymin, ymax = -1,2
# xmin, xmax = .3873709475433,.57073789899
# ymin, ymax = -.1,0
xmin, xmax = -0.161796864652,-0.149089743211
ymin, ymax = 0.091189808841,0.079286297531

iterations = 256
imgx = 1024
imgy = 1024
im = Image.new("RGB", (imgx, imgy))
c = complex(-0.7399999999999998, 0.2999999999999994)
# c = complex(random.random() * 2.0 - 1.0, random.random() - 0.5)
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
	        r = i % 4 * 64
	        g = 0
	        b = i % 16 * 16
        # r = (i*50)%256
        # g = 0
        # b = i
        im.putpixel((x, y), (b + g * 256 + r* 65536))

im.show()
