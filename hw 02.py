# from PIL import Image

# imgx = 512
# imgy = 512
# image = Image.new("RGB",(imgx, imgy))

# image.putpixel((0,0),(255,0,0))

# image.save("drawing.png","PNG ")
from PIL import Image, ImageDraw
im = Image.new('RGB', (512, 512), (255, 0, 0)) 
draw = ImageDraw.Draw(im) 
draw.line((70,0, 70,512), fill=(0, 0, 255), width=10)
draw.line((442,0, 442,512), fill=(0, 0, 255), width=10)
draw.line((0,140, 512,140), fill=(0, 0, 255), width=10)
draw.line((0,140, 512,140), fill=(0, 0, 255), width=10)
draw.line((0,356.6, 512,356.6), fill=(0, 0, 255), width=10)
draw.line((100,170.3, 100,340.6), fill=(0, 0, 255), width=10)
draw.line((200,170.3, 200,340.6), fill=(0, 0, 255), width=10)
draw.line((100,256, 200,256), fill=(0, 0, 255), width=10)
draw.line((300,170.3, 300,340.6), fill=(0, 0, 255), width=10)
draw.line((250,173, 350,173), fill=(0, 0, 255), width=10)
draw.line((250,335, 350,335), fill=(0, 0, 255), width=10)

im.show()

