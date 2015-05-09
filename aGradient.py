from PIL import Image

W, H = map(int, raw_input().split())
r1, g1, b1 = map(int, raw_input().split())
r2, g2, b2 = map(int, raw_input().split())

#def interpolate (c1, c2, x):
#	a =  c1 + int( (float(c2)-float(c1))* (float(x)/float(W)))
#	print c1, c2, x, a
#	return a 
interpolate = lambda c1, c2, x:  c1 + int( (float(c2)-float(c1))* (float(x)/float(W)))

img = Image.new("RGB", (W, 1))
data = img.load()
for x in range(W):
    	data[x, 0] = (interpolate(r1, r2, x), interpolate(g1, g2, x), interpolate(b1, b2, x))
#	print data[x, 0]	

img = img.resize((W, H))
img.show()
