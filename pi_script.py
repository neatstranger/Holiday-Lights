import neopixel
import board
import time
import datetime


pixelCount = 209
pixels = neopixel.NeoPixel(board.D18, pixelCount, auto_write=False)

# Color presets (note: NeoPixel uses (R, G, B) by default)
color_one = (0, 0, 16)
color_two = (0, 16, 0)
color_three = (4, 4, 4)
off = (0, 0, 0)

garage_section = 130
kitchen_section = 209

# Clear everything initially
pixels.fill(off)
pixels.show()

while True:
    print("Showing solid red fade...")
    for red in range(0, 10):
        pixels.fill((0, 0, red))
        pixels.show()
        time.sleep(0.02)

    print("Showing solid green fade...")
    for green in range(0, 10):
        pixels.fill((0, green, 0))
        pixels.show()
        time.sleep(0.02)

    print("Showing solid white fade...")
    for white in range(0, 5):
        pixels.fill((white, white, white))
        pixels.show()
        time.sleep(0.02)

    print("Red and Green alternating...")
    for x in range(0, pixelCount, 2):
        for red in range(0, 25, 2):
            pixels[x] = (0, 0, red)
        if x + 1 < pixelCount:
            for green in range(0, 25, 2):
                pixels[x + 1] = (0, green, 0)
    pixels.show()

    print("Garage/Kitchen sections – mode 1...")
    for x in range(0, 25):
        for pixel in range(0, garage_section):
            pixels[pixel] = (0, 0, x)
        for pixel in range(garage_section, kitchen_section):
            pixels[pixel] = (0, x, 0)
        pixels.show()
        time.sleep(0.05)

    print("Garage/Kitchen sections – mode 2...")
    for x in range(0, 25):
        for pixel in range(0, garage_section):
            pixels[pixel] = (0, x, 0)
        for pixel in range(garage_section, kitchen_section):
            pixels[pixel] = (0, 0, x)
        pixels.show()
        time.sleep(0.05)

    # Short pause between cycles
    time.sleep(1)