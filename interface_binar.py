import random
import cv2
import math
import numpy as np
from tkinter import*
from PIL import Image, ImageDraw, ImageTk
from tkinter import ttk, filedialog

root = Tk()
root.geometry("1600x900")
button1 = Button(root, text="Negativ")
button1.place(x=50, y=10)
button2 = Button(root, text="Prosvet")
button2.place(x=50, y=30)
button3 = Button(root, text="Orttenki")
button3.place(x=50, y=50)
button4 = Button(root, text="Binar")
button4.place(x=50, y=70)
button5 = Button(root, text="Psevdo")
button5.place(x=50, y=90)
button6 = Button(root, text="Roberts")
button6.place(x=50, y=110)
button7 = Button(root, text="Sobel")
button7.place(x=50, y=130)
button11 = Button(root, text="Laplas")
button11.place(x=50, y=150)
button8 = Button(root, text="Kirsh")
button8.place(x=50, y=170)
button9 = Button(root, text="Gistogram")
button9.place(x=50, y=190)
button10 = Button(root, text="Smooth")
button10.place(x=50, y=210)
basewidth = 400
def open_image():
    global image, canvas1, namein,width,height,basewidth
    namein = filedialog.askopenfilename()


    image = Image.open(namein)
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    canvas1 = Canvas(root, width=width, height=height)
    canvas1.configure(background="lightblue")
    canvas1.place(x=100, y=100)
    canvas1.image = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')

num = 0
mode = 0
open_image()
modedraw = 0
# while True:
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
#mode = input("mode: ")

image2 = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)
draw2 = ImageDraw.Draw(image2)

pix = image.load()




def negativ(event):
    global name, draw, num, namein,canvas1,basewidth
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)

    draw = ImageDraw.Draw(image)

    pix = image.load()

    name = "negativ"
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
    num = num + 1
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image.save(name + str(num) + ".jpg", "JPEG")

    del draw

def prosvet(event):
    global name, draw, num, namein,basewidth
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)

    draw = ImageDraw.Draw(image)

    pix = image.load()

    name = "prosvet"
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
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw

def ottenki(event):
    global name, draw, num, namein,basewidth
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)

    draw = ImageDraw.Draw(image)

    pix = image.load()

    name = "ottenkiser"
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = b = c = S
            draw.point((i, j), (a, b, c))
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw

def binar(event):
    global name, draw, num, namein,basewidth
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)

    draw = ImageDraw.Draw(image)

    pix = image.load()

    name = "binar"
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            k=30
            if (a < k):
                a = 0
            if (b < k):
                b = 0
            if (c < k):
                c = 0
            if (a >= k):
                a = 255
            if (b >= k):
                b = 255
            if (c >= k):
                c = 255
            draw.point((i, j), (a, b, c))
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw

def psevdoraskras(event):
    global name, draw, num, namein,basewidth
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    draw = ImageDraw.Draw(image)
    pix = image.load()
    name = "psevdo"
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S <= 85:
                a = 255
                b = 0
                c = 0
            if S > 85 and S <= 170:
                a = 0
                b = 255
                c = 0
            if S > 170 and S <= 255:
                a = 0
                b = 0
                c = 255
            draw.point((i, j), (a, b, c))
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw

def roberts(event):
    global name, draw2, num, namein,basewidth, image2
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    draw2 = ImageDraw.Draw(image2)
    pix = image.load()
    name = "Roberts"
    for i in range(width - 1):
        for j in range(height - 1):
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
            gx = (S1 - S2)
            gy = (S3 - S4)
            S = round((math.sqrt((gx * gx) + (gy * gy))) // 3)
            a = b = c = S
            draw2.point((i, j), (a, b, c))
    wpercent = (basewidth / float(image2.size[0]))
    hsize = int((float(image2.size[1]) * float(wpercent)))
    image2 = image2.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image2)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image2.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw2

def sobel(event):
    global name, draw2, num, namein,basewidth, image2
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    draw2 = ImageDraw.Draw(image2)
    pix = image.load()
    name = "sobel"
    for i in range(2, width - 1):
        for j in range(2, height - 1):
            a1 = pix[i - 1, j - 1][0]
            b1 = pix[i - 1, j - 1][1]
            c1 = pix[i - 1, j - 1][2]
            S1 = (a1 + b1 + c1) // 1
            a2 = pix[i, j - 1][0]
            b2 = pix[i, j - 1][1]
            c2 = pix[i, j - 1][2]
            S2 = (a2 + b2 + c2) // 1
            a3 = pix[i + 1, j - 1][0]
            b3 = pix[i + 1, j - 1][1]
            c3 = pix[i + 1, j - 1][2]
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
            gx = (S7 + S8 * 2 + S9) - (S1 + S2 * 2 + S3)
            gy = (S3 + S6 * 2 + S9) - (S1 + S4 * 2 + S7)
            S = round((math.sqrt((gx * gx) + (gy * gy))) // 3)
            a = b = c = S
            draw2.point((i, j), (a, b, c))
    wpercent = (basewidth / float(image2.size[0]))
    hsize = int((float(image2.size[1]) * float(wpercent)))
    image2 = image2.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image2)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image2.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw2

def kirsh(event):
    global name, draw2, num, namein,basewidth, image2
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    draw2 = ImageDraw.Draw(image2)
    pix = image.load()
    name = "kirsh"
    for i in range(2, width - 1):
        for j in range(2, height - 1):
            a1 = pix[i - 1, j - 1][0]
            b1 = pix[i - 1, j - 1][1]
            c1 = pix[i - 1, j - 1][2]
            S1 = (a1 + b1 + c1) // 1
            a2 = pix[i, j - 1][0]
            b2 = pix[i, j - 1][1]
            c2 = pix[i, j - 1][2]
            S2 = (a2 + b2 + c2) // 1
            a3 = pix[i + 1, j - 1][0]
            b3 = pix[i + 1, j - 1][1]
            c3 = pix[i + 1, j - 1][2]
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
            gx = ((S7 * (-3) + S8 * (-3) + S9 * 5) - (S1 * (-3) + S2 * (-3) + S3 * 5)) * 1
            gy = ((S3 * 5 + S6 * 5 + S9 * 5) - (S1 * (-3) + S4 * (-3) + S7 * (-3))) * 1
            if gx < 0:
                gx = 0
            elif gx > 255:
                gx = 255
            if gy < 0:
                gy = 0
            elif gy > 255:
                gy = 255
            # print(gx)
            # print(gy)
            S = round((math.sqrt((gx * gx) + (gy * gy))) // 3)
            a = b = c = S
            draw2.point((i, j), (a, b, c))
    wpercent = (basewidth / float(image2.size[0]))
    hsize = int((float(image2.size[1]) * float(wpercent)))
    image2 = image2.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image2)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image2.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw2
def alg_laplas(event):
    global name, draw2, num, namein,basewidth
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    draw = ImageDraw.Draw(image)
    pix = image.load()
    name = "laplas"
    # Бинарезация
    print('start')
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0] #узнаём значение красного цвета пикселя
            g = pix[x, y][1] #зелёного
            b = pix[x, y][2] #синего
            sr = (r + g + b) // 3 #среднее значение
            draw.point((x, y), (sr, sr, sr)) #рисуем пиксель

    for x in range(width - 1):
        for y in range(height - 1):
            r = pix[x, y][0] #узнаём значение красного цвета пикселя
            g = pix[x, y][1] #зелёного
            b = pix[x, y][2] #синего
            new_r = pix[x + 1, y][0] + pix[x - 1, y][0] + pix[x, y - 1][0] + pix[x, y + 1][0] - 4 * pix[x, y][0]
            new_g = pix[x + 1, y][1] + pix[x - 1, y][1] + pix[x, y - 1][1] + pix[x, y + 1][1] - 4 * pix[x, y][1]
            new_b = pix[x + 1, y][2] + pix[x - 1, y][2] + pix[x, y - 1][2] + pix[x, y + 1][2] - 4 * pix[x, y][2]
            draw.point((x, y), (new_r, new_g, new_b))
    wpercent = (basewidth / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    image = image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
    image.save(name + str(num) + ".jpg", "JPEG")
    num = num + 1
    del draw
'''
if (mode == "Laplas" or mode == "9"):
    name = "laplas"
    modedraw = 1
    for i in range(2, width - 1):
        for j in range(2, height - 1):
            draw2.point((i, j), (a, b, c))
            draw2.point((i, j + 1), (a, b, c))
            draw2.point((i, j + 2), (a, b, c))
            draw2.point((i + 1, j), (a, b, c))
            draw2.point((i + 1, j + 1), (a * (-2), b * (-2), c * (-2)))
            draw2.point((i + 1, j + 2), (a, b, c))
            draw2.point((i + 2, j), (a * (-1), b * (-1), c * (-1)))
            draw2.point((i + 2, j + 1), (a * (-1), b * (-1), c * (-1)))
            draw2.point((i + 2, j + 2), (a * (-1), b * (-1), c * (-1)))
            #
            #
            draw2.point((i, j), (a * (0), b * (0), c * (0)))
            draw2.point((i, j + 1), (a * (-1), b * (-1), c))
            draw2.point((i, j + 2), (a, b, c))
            draw2.point((i + 1, j), (a, b, c))
            draw2.point((i + 1, j + 1), (a * (-2), b * (-2), c * (-2)))
            draw2.point((i + 1, j + 2), (a, b, c))
            draw2.point((i + 2, j), (a * (-1), b * (-1), c * (-1)))
            draw2.point((i + 2, j + 1), (a * (-1), b * (-1), c * (-1)))
            draw2.point((i + 2, j + 2), (a * (-1), b * (-1), c * (-1)))

            a1 = pix[i - 1, j - 1][0]
            b1 = pix[i - 1, j - 1][1]
            c1 = pix[i - 1, j - 1][2]
            S1 = (a1 + b1 + c1) // 1
            a2 = pix[i, j - 1][0]
            b2 = pix[i, j - 1][1]
            c2 = pix[i, j - 1][2]
            S2 = (a2 + b2 + c2) // 1
            a3 = pix[i + 1, j - 1][0]
            b3 = pix[i + 1, j - 1][1]
            c3 = pix[i + 1, j - 1][2]
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
            gx = ((S7 * (0) + S8 * (1) + S9 * 0))
            gy = S4 * (1) + S5 * (-4) + S6 * 1
            gz = S1 * (0) + S2 * (1) + S3 * 0
            if gx < 0:
                gx = 0
            elif gx > 255:
                gx = 255
            if gy < 0:
                gy = 0
            elif gy > 255:
                gy = 255
            if gz < 0:
                gz = 0
            elif gz > 255:
                gz = 255
            print((gx))
            # print(gx)
            # print(gy)
            S = round((math.sqrt((gx * gx) + (gy * gy) + (gz * gz))) // 3)
            a = b = c = (gx)
            draw2.point((i, j), (a, b, c))
'''
def gistogr(event):
    global name, draw, num, namein,basewidth
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    name = "gistogram.jpg"
    img = cv2.imread(namein, 0)
    equ = cv2.equalizeHist(img)
    cv2.imwrite(name, equ)
    cv2image = Image.open(name)
    wpercent = (basewidth / float(cv2image.size[0]))
    hsize = int((float(cv2image.size[1]) * float(wpercent)))
    cv2image = cv2image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(cv2image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
def smooth(event):
    global name, draw, num, namein
    image = Image.open(namein)
    width = image.size[0]
    print(width)
    height = image.size[1]
    print(height)
    name = "smooth.jpg"
    img = cv2.imread(namein)
    blurred = cv2.GaussianBlur(img, (51, 51), 0)
    cv2.imwrite(name, blurred)
    cv2image = Image.open(name)
    wpercent = (basewidth / float(cv2image.size[0]))
    hsize = int((float(cv2image.size[1]) * float(wpercent)))
    cv2image = cv2image.resize((basewidth, hsize), Image.ANTIALIAS)
    canvas1.image = ImageTk.PhotoImage(cv2image)
    canvas1.create_image(0, 0, image=canvas1.image, anchor='nw')
button1.bind("<Button-1>", negativ)
button2.bind("<Button-1>", prosvet)
button3.bind("<Button-1>", ottenki)
button4.bind("<Button-1>", binar)
button5.bind("<Button-1>", psevdoraskras)
button6.bind("<Button-1>", roberts)
button7.bind("<Button-1>", sobel)
button8.bind("<Button-1>", kirsh)
button9.bind("<Button-1>", gistogr)
button10.bind("<Button-1>", smooth)
button11.bind("<Button-1>", alg_laplas)

root = mainloop()