import random
import cv2
import math
import numpy as np
from PIL import Image, ImageDraw

num=0
mode=0
namein="temp.jpg"
modedraw = 0
while True:
	print('''
	Select type:
	Negativ 1
	Prosvet 2
	Ottenki Serogo 3
	Binar 4
	Psevdoraskras 5
	Gistogramm 6
	Smooth 7
	''')
	'''
	mode=int(mode)
	mode = mode+1
	mode=str(mode)
	print(mode)
	'''
	mode=input("mode: ")
	image = Image.open(namein)
	width = image.size[0]
	print(width)
	height = image.size[1]
	print(height)
	image2=Image.new("RGB",(width,height))
	draw = ImageDraw.Draw(image)
	draw2=ImageDraw.Draw(image2)

	pix = image.load()

	if (mode == "Negaiv" or mode == "1"):
		modedraw = 0
		name="negativ"
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0]
				b = pix[i, j][1]
				c = pix[i, j][2]
				draw.point((i, j), (255 - a, 255 - b, 255 - c))
	if (mode == "Prosvet" or mode == "2"):
		modedraw = 0
		name="prosvet"
		factor = 100
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0] + factor
				b = pix[i, j][1] + factor
				c = pix[i, j][2] + factor
				if (a < 0):
					a = 0
				if (b < 0):
					b = 0
				if (c < 0):
					c = 0
				if (a > 255):
					a = 255
				if (b > 255):
					b = 255
				if (c > 255):
					c = 255
				draw.point((i, j), (a, b, c))
	if (mode == "Ottenki Serogo" or mode == "3"):
		modedraw = 0
		name="ottenkiser"
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0]
				b = pix[i, j][1]
				c = pix[i, j][2]
				S = (a + b + c) // 3
				a = b = c = S
				draw.point((i, j), (a, b, c))
	if (mode == "Binar" or mode == "4"):
		modedraw = 0
		name="binar"
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0]
				b = pix[i, j][1]
				c = pix[i, j][2]
				if (a < 128):
					a = 0
				if (b < 128):
					b = 0
				if (c < 128):
					c = 0
				if (a >= 128):
					a = 255
				if (b >= 128):
					b = 255
				if (c >= 128):
					c = 255
				draw.point((i, j), (a, b, c))
	if (mode == "Psevdaraskras" or mode == "5"):
		modedraw = 0
		name="psevdo"
		'''image = Image.open("ottenkiser" + str(num - 1) + ".jpg")
		draw = ImageDraw.Draw(image)
		width = image.size[0]
		height = image.size[1]
		pix = image.load()'''
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0]
				b = pix[i, j][1]
				c = pix[i, j][2]
				S=a+b+c
				if S<=85:
					a=255
					b=0
					c=0
				if S>85 and S <= 170:
					a = 0
					b = 255
					c = 0
				if S>170 and S<=255:
					a=0
					b=0
					c=255
				draw.point((i, j), (a, b, c))
	if (mode == "color" or mode == "88"):
		name="sobelcolor"
		modedraw=1
		for i in range(2,width-1):
			for j in range(2,height-1):
				a1 = pix[i-1, j-1][0]
				b1 = pix[i-1, j-1][1]
				c1 = pix[i-1, j-1][2]
				S1 = (a1 + b1 + c1)//1
				a2 = pix[i, j - 1][0]
				b2 = pix[i, j - 1][1]
				c2 = pix[i, j - 1][2]
				S2 = (a2 + b2 + c2) // 1
				a3 = pix[i+1, j -1][0]
				b3 = pix[i+1, j -1][1]
				c3 = pix[i+1, j -1][2]
				S3 = (a3 + b3 + c3) // 1
				a4 = pix[i - 1, j][0]
				b4 = pix[i - 1, j][1]
				c4 = pix[i - 1, j][2]
				S4 = (a4 + b4 + c4) // 1
				a5 = pix[i, j][0]
				b5 = pix[i, j][1]
				c5 = pix[i, j][2]
				S5 = (a5 + b5 + c5) // 1
				a6 = pix[i + 1, j][0]
				b6 = pix[i + 1, j][1]
				c6 = pix[i + 1, j][2]
				S6 = (a6 + b6 + c6) // 1
				a7 = pix[i - 1, j + 1][0]
				b7 = pix[i - 1, j + 1][1]
				c7 = pix[i - 1, j + 1][2]
				S7 = (a7 + b7 + c7) // 1
				a8 = pix[i, j + 1][0]
				b8 = pix[i, j + 1][1]
				c8 = pix[i, j + 1][2]
				S8 = (a8 + b8 + c8) // 1
				a9 = pix[i + 1, j + 1][0]
				b9 = pix[i + 1, j + 1][1]
				c9 = pix[i + 1, j + 1][2]
				S9 = (a9 + b9 + c9) // 1
				gxa = (a7 + a8*2 + a9) - (a1 + a2*2 + a3)
				gya = (a3 + a6*2 + a9) - (a1 + a4*2 + a7)
				gxb = (b7 + b8 * 2 + b9) - (b1 + b2 * 2 + b3)
				gyb = (b3 + b6 * 2 + b9) - (b1 + b4 * 2 + b7)
				gxc = (c7 + c8 * 2 + c9) - (c1 + c2 * 2 + c3)
				gyc = (c3 + c6 * 2 + c9) - (c1 + c4 * 2 + c7)
				a=round((math.sqrt((gxa*gxa)+(gya*gya)))//3)
				b = round((math.sqrt((gxb * gxb) + (gyb * gyb))) // 3)
				c = round((math.sqrt((gxc * gxc) + (gyc * gyc))) // 3)
				draw2.point((i, j), (a, b, c))
	if (mode == "Roberts" or mode == "6"):
		name="roberts"
		modedraw=1
		for i in range(width-1):
			for j in range(height-1):
				a1 = pix[i, j][0]
				b1 = pix[i, j][1]
				c1 = pix[i, j][2]
				S1 = (a1 + b1 + c1) // 1
				a2 = pix[i + 1, j + 1][0]
				b2 = pix[i + 1, j + 1][1]
				c2 = pix[i + 1, j + 1][2]
				S2 = (a2 + b2 + c2) // 1
				a3 = pix[i + 1, j][0]
				b3 = pix[i + 1, j][1]
				c3 = pix[i + 1, j][2]
				S3 = (a3 + b3 + c3) // 1
				a4 = pix[i, j + 1][0]
				b4 = pix[i, j + 1][1]
				c4 = pix[i, j + 1][2]
				S4 = (a4 + b4 + c4) // 1
				gx = (S1-S2)
				gy = (S3-S4)
				S=round((math.sqrt((gx*gx)+(gy*gy)))//3)
				a=b=c=S
				draw2.point((i, j), (a, b, c))
	if (mode == "Sobel" or mode == "7"):
		name="sobel"
		modedraw=1
		for i in range(2,width-1):
			for j in range(2,height-1):
				a1 = pix[i-1, j-1][0]
				b1 = pix[i-1, j-1][1]
				c1 = pix[i-1, j-1][2]
				S1 = (a1 + b1 + c1)//1
				a2 = pix[i, j - 1][0]
				b2 = pix[i, j - 1][1]
				c2 = pix[i, j - 1][2]
				S2 = (a2 + b2 + c2) // 1
				a3 = pix[i+1, j -1][0]
				b3 = pix[i+1, j -1][1]
				c3 = pix[i+1, j -1][2]
				S3 = (a3 + b3 + c3) // 1
				a4 = pix[i - 1, j][0]
				b4 = pix[i - 1, j][1]
				c4 = pix[i - 1, j][2]
				S4 = (a4 + b4 + c4) // 1
				a5 = pix[i, j][0]
				b5 = pix[i, j][1]
				c5 = pix[i, j][2]
				S5 = (a5 + b5 + c5) // 1
				a6 = pix[i + 1, j][0]
				b6 = pix[i + 1, j][1]
				c6 = pix[i + 1, j][2]
				S6 = (a6 + b6 + c6) // 1
				a7 = pix[i - 1, j + 1][0]
				b7 = pix[i - 1, j + 1][1]
				c7 = pix[i - 1, j + 1][2]
				S7 = (a7 + b7 + c7) // 1
				a8 = pix[i, j + 1][0]
				b8 = pix[i, j + 1][1]
				c8 = pix[i, j + 1][2]
				S8 = (a8 + b8 + c8) // 1
				a9 = pix[i + 1, j + 1][0]
				b9 = pix[i + 1, j + 1][1]
				c9 = pix[i + 1, j + 1][2]
				S9 = (a9 + b9 + c9) // 1
				gx = (S7 + S8*2 + S9) - (S1 + S2*2 + S3)
				gy = (S3 + S6*2 + S9) - (S1 + S4*2 + S7)
				S=round((math.sqrt((gx*gx)+(gy*gy)))//3)
				a=b=c=S
				draw2.point((i, j), (a, b, c))
	if (mode == "Kirsh" or mode == "8"):
		name="kirsh"
		modedraw=1
		for i in range(2,width-1):
			for j in range(2,height-1):
				a1 = pix[i-1, j-1][0]
				b1 = pix[i-1, j-1][1]
				c1 = pix[i-1, j-1][2]
				S1 = (a1 + b1 + c1)//1
				a2 = pix[i, j - 1][0]
				b2 = pix[i, j - 1][1]
				c2 = pix[i, j - 1][2]
				S2 = (a2 + b2 + c2) // 1
				a3 = pix[i+1, j -1][0]
				b3 = pix[i+1, j -1][1]
				c3 = pix[i+1, j -1][2]
				S3 = (a3 + b3 + c3) // 1
				a4 = pix[i - 1, j][0]
				b4 = pix[i - 1, j][1]
				c4 = pix[i - 1, j][2]
				S4 = (a4 + b4 + c4) // 1
				a5 = pix[i, j][0]
				b5 = pix[i, j][1]
				c5 = pix[i, j][2]
				S5 = (a5 + b5 + c5) // 1
				a6 = pix[i + 1, j][0]
				b6 = pix[i + 1, j][1]
				c6 = pix[i + 1, j][2]
				S6 = (a6 + b6 + c6) // 1
				a7 = pix[i - 1, j + 1][0]
				b7 = pix[i - 1, j + 1][1]
				c7 = pix[i - 1, j + 1][2]
				S7 = (a7 + b7 + c7) // 1
				a8 = pix[i, j + 1][0]
				b8 = pix[i, j + 1][1]
				c8 = pix[i, j + 1][2]
				S8 = (a8 + b8 + c8) // 1
				a9 = pix[i + 1, j + 1][0]
				b9 = pix[i + 1, j + 1][1]
				c9 = pix[i + 1, j + 1][2]
				S9 = (a9 + b9 + c9) // 1
				gx = ((S7*(-3) + S8*(-3) + S9*5) - (S1*(-3) + S2*(-3) + S3*5))*1
				gy = ((S3*5 + S6*5 + S9*5) - (S1*(-3) + S4*(-3) + S7*(-3)))*1
				if gx<0:
					gx=0
				elif gx>255:
					gx=255
				if gy<0:
					gy=0
				elif gy>255:
					gy=255
				#print(gx)
				#print(gy)
				S=round((math.sqrt((gx*gx)+(gy*gy)))//3)
				a=b=c=S
				draw2.point((i, j), (a, b, c))
	if (mode == "Laplas" or mode == "9"):
		name="laplas"
		modedraw=1
		for i in range(2,width-1):
			for j in range(2,height-1):
				draw2.point((i, j), (a, b, c))
				draw2.point((i, j+1), (a, b, c))
				draw2.point((i, j+2), (a, b, c))
				draw2.point((i+1, j), (a, b, c))
				draw2.point((i+1, j+1), (a*(-2), b*(-2), c*(-2)))
				draw2.point((i + 1, j+2), (a, b, c))
				draw2.point((i +2, j ), (a * (-1), b * (-1), c * (-1)))
				draw2.point((i + 2, j+1), (a * (-1), b * (-1), c * (-1)))
				draw2.point((i + 2, j+2), (a * (-1), b * (-1), c * (-1)))
				#
				#
				draw2.point((i, j), (a*(0), b*(0), c*(0)))
				draw2.point((i, j + 1), (a*(-1), b*(-1), c))
				draw2.point((i, j + 2), (a, b, c))
				draw2.point((i + 1, j), (a, b, c))
				draw2.point((i + 1, j + 1), (a * (-2), b * (-2), c * (-2)))
				draw2.point((i + 1, j + 2), (a, b, c))
				draw2.point((i + 2, j), (a * (-1), b * (-1), c * (-1)))
				draw2.point((i + 2, j + 1), (a * (-1), b * (-1), c * (-1)))
				draw2.point((i + 2, j + 2), (a * (-1), b * (-1), c * (-1)))

				a1 = pix[i-1, j-1][0]
				b1 = pix[i-1, j-1][1]
				c1 = pix[i-1, j-1][2]
				S1 = (a1 + b1 + c1)//1
				a2 = pix[i, j - 1][0]
				b2 = pix[i, j - 1][1]
				c2 = pix[i, j - 1][2]
				S2 = (a2 + b2 + c2) // 1
				a3 = pix[i+1, j -1][0]
				b3 = pix[i+1, j -1][1]
				c3 = pix[i+1, j -1][2]
				S3 = (a3 + b3 + c3) // 1
				a4 = pix[i - 1, j][0]
				b4 = pix[i - 1, j][1]
				c4 = pix[i - 1, j][2]
				S4 = (a4 + b4 + c4) // 1
				a5 = pix[i, j][0]
				b5 = pix[i, j][1]
				c5 = pix[i, j][2]
				S5 = (a5 + b5 + c5) // 1
				a6 = pix[i + 1, j][0]
				b6 = pix[i + 1, j][1]
				c6 = pix[i + 1, j][2]
				S6 = (a6 + b6 + c6) // 1
				a7 = pix[i - 1, j + 1][0]
				b7 = pix[i - 1, j + 1][1]
				c7 = pix[i - 1, j + 1][2]
				S7 = (a7 + b7 + c7) // 1
				a8 = pix[i, j + 1][0]
				b8 = pix[i, j + 1][1]
				c8 = pix[i, j + 1][2]
				S8 = (a8 + b8 + c8) // 1
				a9 = pix[i + 1, j + 1][0]
				b9 = pix[i + 1, j + 1][1]
				c9 = pix[i + 1, j + 1][2]
				S9 = (a9 + b9 + c9) // 1
				gx = ((S7*(0) + S8*(1) + S9*0) )
				gy=S4*(1) + S5*(-4) + S6*1
				gz=S1*(0) + S2*(1) + S3*0
				if gx<0:
					gx=0
				elif gx>255:
					gx=255
				if gy<0:
					gy=0
				elif gy>255:
					gy=255
				if gz<0:
					gz=0
				elif gz>255:
					gz=255
				print((gx))
				#print(gx)
				#print(gy)
				S=round((math.sqrt((gx*gx)+(gy*gy)+(gz*gz)))//3)
				a=b=c=(gx)
				draw2.point((i, j), (a, b, c))
	if (mode == "Gistogramm" or mode == "6"):
		name="gistogram.jpg"
		img = cv2.imread(namein,0)
		equ = cv2.equalizeHist(img)
		cv2.imwrite(name, equ)
	elif (mode == "Smooth" or mode == "7"):
		name = "smooth.jpg"
		img = cv2.imread(namein)
		blurred = cv2.GaussianBlur(img, (51, 51), 0)
		cv2.imwrite(name, blurred)
	elif modedraw==1:
		image2.save(name + str(num) + ".jpg", "JPEG")
		num = num + 1
		del draw2
	else:
		image.save(name+str(num)+".jpg", "JPEG")
		num=num+1
		del draw