from PIL import Image, ImageDraw
import math

img = Image.new('RGB', (960, 960), (255, 255, 255))
draw = ImageDraw.Draw(img)
angle = math.radians(70)

with open("D:\Study\Python files\Comp_Graphics\Laboratory 2\DS6.txt", "r") as file:
    for line in file:
        coords_list = line.split()
        i = int(coords_list[0])-480
        j = int(coords_list[1])-480
        x = i*math.cos(angle) - j*math.sin(angle)
        y = i*math.sin(angle) + j*math.cos(angle)
        draw.line((x+480, y+480, x+481, y+481), fill=(0, 0, 255))

img.show()
img.save('result2.png')