import sys
from PIL import Image

im = Image.open(sys.argv[1])

width, height = im.size

pixels = im.tobytes()

no_color = int(len(pixels)/(width*height))

dmax = 0
area = 0
### NAIVE IMPLEMENTATION ####
#area = pixels.count(b'\x00')/no_color
#dmax = max(pixels[i*no_color:(i + width)*no_color].count(b'\x00') for i in range(width*height))/no_color

#for y in range(height):
    #d = 0
    #for x in range(width):
        #index = (y * width + x) * no_color
        #if pixels[index:index + 3] == b'\x00\x00\x00':
            #d += 1
            #area += 1
    #if d > dmax:
        #dmax = d

#print('Area     :', area)
    #print('No circle found!')
#print('Diameter :', dmax)
#print((area*4)/(dmax*dmax))


done = []
in_progress = []

for y in range(height):
    for x in range(width):
        index = (y * width + x) * no_color


