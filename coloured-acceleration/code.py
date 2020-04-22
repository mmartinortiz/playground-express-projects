"""
Set colours on the led according to the accelerometer values:

- X Axis: Red
- Y Axis: Green
- Z Axis: Blue

If the Playground Express is steady, the gravity will "attract"
one of the accelerometer axis (check the surface of the PE)
depending on the PE position. The led will get coloured according
to the value of the axis.

If, for example, the gravity only attracts the Z axis, because
the PE lays on a table with the led facing up, the led will
become blue.
"""
from adafruit_circuitplayground import cp

while True:
    # Set the ground value of the colours
    red = 0
    green = 0
    blue = 0

    # Read accelerometer values
    x, y, z = cp.acceleration

    # When using Mu Editor, the values can be seen on the Plotter
    print((x, y, z))

    # Set the colour for all the leds related to the x, y and z values
    cp.pixels.fill(((red + abs(int(x))), (green + abs(int(y))), (blue + abs(int(z)))))