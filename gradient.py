# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

pixel_pin = board.D18

num_pixels = 150

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.9, auto_write=False,
                           pixel_order=ORDER)


def init_colors():
    pixels = [(i,0,0) for i in range(num_pixels)]


def gradient_cycle(wait):
    for i in range(len(pixels) - 1):
        pixels[i] = pixels[i+1]

    temp = pixels[-1]
    to_change = (1,0,0)
    if temp[0] >= 255 and temp[1] <= 255 and temp[2] == 0:
        to_change = (0,1,0)
    if temp[0] > 0 and temp[1] >= 255 and temp[2] == 0:
        to_change = (-1,0,0)
    if temp[0] == 0 and temp[1] >= 255 and temp[2] < 255:
        to_change = (0,0,1)
    if temp[0] == 0 and temp[1] > 0 and temp[2] >= 255:
        to_change = (0,-1,0)
    if temp[0] < 255 and temp[1] == 0 and temp[2] >= 255:
        to_change = (1,0,0)
    if temp[0] >= 255 and temp[1] == 0 and temp[2] > 0:
        to_change = (0,0,-1) 
    
    pixels[-1] = (pixels[-1][0] + to_change[0], pixels[-1][1] + to_change[1], pixels[-1][2] + to_change[2])

    pixels.show()
    time.sleep(wait)



init_colors()
time.sleep(1)

while True:

    gradient_cycle(0.01)

    # pixels.fill((0, 0, 0))
    # # Uncomment this line if you have RGBW/GRBW NeoPixels
    # # pixels.fill((0, 0, 255, 0))
    # pixels.show()
    # time.sleep(1)

    # rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step