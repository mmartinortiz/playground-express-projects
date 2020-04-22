"""
Set a random colour (red, green or blue) to each led on the Playground
"""
import time
from random import choice
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1

def get_color():
    # Returns a random colour: red, blue or green
    colours = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]
    return choice(colours)

while True:
    for i in range(len(cp.pixels)):
        # Set a random colour to each led
        cp.pixels[i] = get_color()

    time.sleep(0.1)