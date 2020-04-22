# Coloured acceleration

Based on the Adafruit's tutorial "[acceleration](https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/acceleration)".

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
