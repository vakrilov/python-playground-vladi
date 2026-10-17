# Lesson 1: Your first shapes!
# Run this program, then try changing the numbers and colors.

from drawing import *

background("lightblue")

circle(400, 300, 100, "yellow")             # x, y, radius, color
rectangle(50, 50, 200, 100, "red")          # x, y, width, height, color
triangle(600, 500, 700, 350, 800, 500, "green")
square(100, 400, 120, "purple")
line(0, 590, 800, 590, "black", 5)

text("Hello, I can code!", 250, 20, "darkblue", 48)

# Challenge: make the yellow circle bigger. Then add a blue circle on the right.
