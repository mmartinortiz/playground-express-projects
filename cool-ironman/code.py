"""
Cool or Angry IronMan

The NeoPixel brightness change across time, if button A is pressed,
the color change from white to red, or viceversa
"""
import time
from adafruit_circuitplayground import cp

brightness = 0.1
increasing = True
cp.pixels.auto_write = False
cp.pixels.brightness = brightness

# Flag for detecting when the button is pressed and released
button_pressed = False

white = (255, 255, 255)
red = (255, 0, 0)

def set_pixels_color(color):
    for i in range(len(cp.pixels)):
        cp.pixels[i] = color

# Start cool
color = white
set_pixels_color(white)
cp.pixels.show()

# Brightness is changed along 10 steps
step = 1
steps = 10

while True:
    cp.pixels.brightness = step / steps

    step = step + 1 if increasing else step - 1

    # Change the brightness increase/decrease
    # if we go out of boundaries
    if step >= steps or step <= 1:
        increasing = not increasing

    # Check if the button has been released
    if not cp.button_a and button_pressed:
        # Button has been released!
        button_pressed = False

    # Check if the button has been pressed
    if cp.button_a and not button_pressed:
        # Change color of pixels
        color = white if color == red else red
        set_pixels_color(color)

        button_pressed = True

    cp.pixels.show()
    time.sleep(0.1)
