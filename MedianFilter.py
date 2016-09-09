'''
Phuc Pham
CST205
9/9/16

This program takes in 9 images and create a new image with the unchanging
background. It removes the inconsistency in the images.
'''

import statistics

#arrays to store RGB values
red = []
green = []
blue = []

#array to store all the RGB of the 9 pictures
pic = []

w = 495
h = 557

i = 0

#open 9 images
from PIL import Image
img1 = Image.open('1.png')
img2 = Image.open('2.png')
img3 = Image.open('3.png')
img4 = Image.open('4.png')
img5 = Image.open('5.png')
img6 = Image.open('6.png')
img7 = Image.open('7.png')
img8 = Image.open('8.png')
img9 = Image.open('9.png')

#load 9 images
img1data = img1.load()
img2data = img2.load()
img3data = img3.load()
img4data = img4.load()
img5data = img5.load()
img6data = img6.load()
img7data = img7.load()
img8data = img8.load()
img9data = img9.load()

#new empty image
img10 = Image.new("RGB",(w, h))
img11 = img10.getdata()

#put image data of 9 images in array
pixels = [img1data, img2data, img3data, img4data, img5data, img6data, img7data, img8data, img9data]

#loop through the 9 images to find the median rgb
for x in range(0 , w):
	for y in range(0, h):
		for j in pixels:			#find rgb for pixel at (x,y)
			redp = j[x,y][0]		#find red value
			greenp = j[x,y][1]		#find green value
			bluep = j[x,y][2]		#find blue value
			
			red.append(redp)		#put red value in red[]
			green.append(greenp)	#put green value in green[]
			blue.append(bluep)		#put blue value in blue[]
			
			#sorting rgb 
			red.sort()				
			green.sort()
			blue.sort()
			
		#find median
		medianred = statistics.median(red)
		mediangreen = statistics.median(green)
		medianblue = statistics.median(blue)
		
		#put median in rgb
		rgb = (medianred, mediangreen, medianblue)
		
		#clear the 3 arrays
		red = []
		green = []
		blue = []
		
		#put pixel in new image
		img10.putpixel((x,y), rgb)
	
#show new image	
img10.show()