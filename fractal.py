from PIL import Image, ImageDraw
width = 512
height = 512
im = Image.new('RGB', (width,height), (255, 0, 0))
max_iterations = 50
for i in range(width):
	for j in range(height):
		z = 0
		c = complex(i,j)
		iterations = 0
		while abs(z) <= 2 and iterations < max_iterations:
			z = z**2 + c
			iterations += 1
im.show()
