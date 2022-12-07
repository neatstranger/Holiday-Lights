import neopixel
import board
import time
import datetime

#garage first corner pixel =  22
#top of the garage roof = pixel 59
#Garage Second Corner Pixel = 95
#Front door left last pixel = 130


#Front door right first pixel = 131
#kitchen first corner pixel =  160
#top of the kitchen roof = pixel 182
#second kitchen corner pixel = 205


#For some reason the colors aren't right
#(blue,green,red)


pixelCount = 209
pixels = neopixel.NeoPixel(board.D18, pixelCount)

color_one = (0,0,16)
color_two = (0,16,0)
color_three = (4,4,4)
off = (0, 0, 0)

garage_section = 130
kitchen_section = 209

pixels.fill((0,0,0))
while True:
    pixels.auto_write = True
    while (datetime.datetime.now().hour >= 17 and datetime.datetime.now().hour <= 23) or (datetime.datetime.now().hour >= 4 and datetime.datetime.now().hour <= 7) :
        red = 0
        while red < 10:
            pixels.fill((0,0,red))
            red += 0.1
        green = 0
        while green < 10:
            pixels.fill((0,green,0))
            green += 0.1
        white = 0
        while white < 5:
            pixels.fill((white, white, white))
            white += 0.1
        x = 0

        while x < pixelCount -1:
            red = 0 
            while red < 25:
               pixels[x] = (0,0,red) 
               red += 2
            green = 0
            while green < 25:
               pixels[x+1] = (0,green,0)
               green +=2
            x += 2
        pixels.auto_write = False

        for x in range(0,25):
            for pixel in range(0,garage_section):
                pixels[pixel] = (0,0,x)
            for pixel in range(garage_section, kitchen_section):
                pixels[pixel] = (0,x,0)
            pixels.show()
            time.sleep(0.5)
        for x in range(0,25):
            for pixel in range(0,garage_section):
                pixels[pixel] = (0,25,0)
            for pixel in range(garage_section, kitchen_section):
                pixels[pixel] = (0,0,25)
            pixels.show()
            time.sleep(0.5)
        
        time.sleep(10)
        


# while True:
#     while datetime.datetime.now().hour >= 17 and datetime.datetime.now().hour <= 22:
#         for currentPixel in range(pixelCount):
#             time.sleep(0.075)
#             pixels[currentPixel] = color_one
#         for currentPixel in range(pixelCount-1, 0, -1):
#             time.sleep(0.1)
#             pixels[currentPixel] =  color_one
#         for currentPixel in range(pixelCount):
#             time.sleep(0.075)
#             pixels[currentPixel] = off
#     pixels.fill((0,0,0))
#     time.sleep(600)
