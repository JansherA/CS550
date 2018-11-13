#Complex class for Mandlebrot project
#Jansher Azmat
#Sources: Math library and Mandlebrot introduction in class excersize sheet
#Submitted November 12, 2018
#On my honor, I have neither given nor received unauthorized aid ~Jansher

#EXPLANATION: (all one paragraph)
# Through my trials testing both the built-in python method versus my manual Complex class, I have concluded that the differences between the two versions are inconsistence and minuscule. I believe the rationale for this finding is that the complex class - in general - (both my version and the built-in method) is only a fraction of the actual execution time. 
# The majority of the average time it took to run both programs (roughly 16 seconds) originated from the image being drawn and rendered rather than the math involved. Even if the math in the built-in method were more efficient than the class I created, this difference would practically have little-to-no effect on the execution time. 
# The bulk of the execution time is derived from the image processing -- as opposed to the math. I proved this through running several trials changing the zoom of the fractal its C value (shape). Each one of the changes I made, such as zooming out, greatly effected the time that the program took to process (with a normal zoom of -2, 2; the code only took 2-3 seconds versus 16+ seconds for the custom cool-looking zoom I selected) proving that the math has very little to do with the time it takes for the program it takes. 
# Thus, making the classes equivalent in productivity. 


#This is imported for math.sqrt since square root isn't incorporated in python
import math 

#Here is my class to replace the built in complex class
#The built in complex class has a lowercase c, so I had to make the C capital for my own class so the system wouldn't try and use the built in class
class Complex: 


	#Here I am creating the constructor for the real and imaginary parts
	def __init__(self, re, im): 

		#Here, self is a variable that can be accessed at any time and an instance of the class	
		self.re = re  
		
		#Inside of this instance is where re and im are stored.		
		self.im = im 
		
	#Adding together two numbers, lets say a and b (a+b), is processed by python as a.__add__(b). Here, a is stored as self (which as aforementioned, self can be accessed at any time) and b is the number being receieved and stored in the variable 'b' which is why it is defined in the method
	def __add__(self, b): #This method is used to add real and imaginary parts, this is step 3 in the mandelbrot calculation where you add z and c together

		#Here is the actual calculation to add imaginary numbers z and c
		return Complex(self.re + b.re, self.im + b.im) 

	#This method is also used in the mandelbrot calculation to multiple z1 by z1
	def __mul__(self, b): 
		
		#Here is the actual calculation with self.im, self.re, b.re, and b.im instead of x1, x2, y1, y2
		return (self.re * b.re - self.im * b.im,self.im * b.re + b.im * b.im) 
	
	#Pow is the keyword for the exponent operation with the same variables self and b
	def __pow__(self, b): 

		#This is the second step in the Mandelbrot function where z is squared. Traditionally, the value of z is x, y. These variables x (the real part) and y (the imaginary part) are stored in self.re and self.im
		return Complex(self.re**2 - self.im**2, 2*self.re*self.im)
	
	#This is the first step of the mandelbrot calculation where you have to take the absolute value of z
	def __abs__(self):

		#The absolute value of z is the sqrt of the real part squared (x, or in this case self.re) and the imaginary part squared (y, or in this case self.im)
		return math.sqrt(self.re**2 + self.im**2)


from PIL import Image

#This is a library that allowes me to time when the code is initially entered in terminal to when the picture of the fractal is generated
from timeit import default_timer as t
start = t()
import random

xmin, xmax = -0.156998049092, -0.149590664054
ymin, ymax = 0.087830637949,0.082645468422

#Uncomment this and comment out the two lines above if you want to randomly generate the shape of the fractal.
# xmin, xmax = -2, 2
# ymin, ymax = -2, 2

iterations = 256
imgx = 1024
imgy = 1024
im = Image.new("RGB", (imgx, imgy))


c = complex(-0.7399999999999998, 0.2999999999999994)

#In Julia's set, c defined the shape of the fractal. Use this line below to randomly generate the shape of the fractal, if you're into that. *be sure to comment out the line above this and comment out the specific zoom above for the zoom -2, 2 (commented out) if you want to try the random shape
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