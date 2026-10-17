# Lesson 2: Draw a house by putting shapes together.

from drawing import *

background("skyblue")

# grass
rectangle(0, 450, 800, 150, "forestgreen")

# sun
circle(700, 100, 60, "gold")

# house walls
rectangle(250, 250, 300, 220, "burlywood")

# roof (a triangle on top of the walls)
triangle(230, 250, 400, 120, 570, 250, "firebrick")

# door
rectangle(370, 360, 60, 110, "saddlebrown")
circle(420, 415, 5, "gold")   # door knob

# windows
square(280, 290, 60, "lightyellow")
square(460, 290, 60, "lightyellow")
square(280, 290, 60, "black", outline=3)   # outline=3 draws just the edge
square(460, 290, 60, "black", outline=3)

# Challenge: add a chimney, a tree, or some clouds (clouds = a few white circles!)
