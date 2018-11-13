#Mandlebrot and Julia's set fractal images
#Jansher Azmat
#No Sources
#Submitted Oct. 25
#Two Mandlebrot Images went smoothly and the transition to the Julia's set was quite easy
#On my honor, I have neither given nor received unauthorized aid


from PIL import Image
width = 200
height = 200
im = Image.new('RGB', (width,height), (0, 0, 0))
xmin, xmax = -0.505264557414, -0.502887081893
ymin, ymax = -0.608373302711, -0.606709069846
# xmin, xmax = -2, 2
# ymin, ymax = -2, 2
max_iterations = 256
for x in range(width):
	for y in range(height):
		cy = y * (ymax-ymin) / (height-1) +ymin
		cx = x * (xmax-xmin) / (width-1) +xmin
		c = complex(cx, cy)
		z = 0
		iterations = 0
		while abs(z) <= 2 and iterations <= max_iterations:
			z = z**2 + c
			iterations += 1

		if iterations > 250: #This if statement guarentees the color of the middle of the fractal (max iterations) to be whatever I choose
			r = 30
			g = 144
			b = 255
		else: 
			r = (iterations*50)%256
			g = 0
			b = iterations

		im.putpixel((x,y), (r,g,b))
im.show()

width = 200
height = 200
im = Image.new('RGB', (width,height), (0, 0, 0))
xmin, xmax = -0.755428, -0.74428
ymin, ymax = -0.1230009, -0.1130009
# xmin, xmax = -2, 2
# ymin, ymax = -2, 2
max_iterations = 256
for x in range(width):
	for y in range(height):
		cy = y * (ymax-ymin) / (height-1) +ymin
		cx = x * (xmax-xmin) / (width-1) +xmin
		c = complex(cx, cy)
		z = 0
		iterations = 0
		while abs(z) <= 2 and iterations <= max_iterations:
			z = z**2 + c
			iterations += 1
		# r = 255 - iterations
		# g = (iterations*50)%256
		# b = iterations-50

		# r = iterations + 100
		# g = (iterations*50)%256
		# b = 255

		# r = (iterations*50)%256
		# g = 0
		# b = 400 - iterations

		# r = iterations - 255
		# g = (iterations*50)%256
		# b = 135

		if iterations > 250: #This if statement guarentees the color of the middle of the fractal (max iterations) to be whatever I choose
			r = 255 - iterations
			g = (iterations*50)%256
			b = iterations-50
		else: 
			r = (iterations*50)%256
			g = 0
			b = 400 - iterations

		# r = (iterations*50)%256
		# g = 191- iterations
		# b = 255
		im.putpixel((x,y), (r,g,b))
im.show()

import random
xmin, xmax = -1.5,0
ymin, ymax = -1,2
# xmin, xmax = .3873709475433,.57073789899
# ymin, ymax = -.1,0

iterations = 256
imgx = 200
imgy = 200
im = Image.new("RGB", (imgx, imgy))
c = complex(.5, .5)
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

