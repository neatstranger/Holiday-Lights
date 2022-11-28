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

pixels.fill((0,0,0))
while True:
    while datetime.datetime.now().hour >= 17 and datetime.datetime.now().hour <= 22:
        x = 0
        while x <= pixelCount:
            pixels[x] = color_one
            pixels[x+1] = color_two
            #pixels[x+2] = color_three

            x += 2

        time.sleep(600)


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