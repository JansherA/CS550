from PIL import Image
import random
xmin, xmax = -2.0, 1
ymin, ymax = -1.5, 1.5
iterations = 256
imgx = 512
imgy = 512
im = Image.new("RGB", (imgx, imgy))
c = complex(random.random() * 2.0 - 1.0, random.random() - 0.5)

for y in range(imgy):
    zy = y * (ymax - ymin) / (imgy - 1)  + ymin
    for x in range(imgx):
        zx = x * (xmax - xmin) / (imgx - 1) + xmin
        z = complex(zx, zy)
        for i in range(iterations):
            if abs(z) > 2.0: 
                break 
            z = z**2 + c 
        # if iterations > 250: #This if statement guarentees the color of the middle of the fractal (max iterations) to be whatever I choose
        #     r = 30
        #     g = 144
        #     b = 255
        # else: 
        # r = i % 4 * 64
        # g = i % 8 * 32
        # b = i % 16 * 16
        r = 255 - i
        g = (i*50)%256
        b = i-50
        im.putpixel((x, y), (b + g * 256 + r* 65536))

im.show()