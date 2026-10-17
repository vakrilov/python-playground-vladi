# Lesson 4: Random art! Every time you run it, you get a new picture.

import random
from drawing import *

background("white")

for i in range(100):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    size = random.randint(10, 60)
    circle(x, y, size, random_color())

for i in range(15):
    star(random.randint(0, 800), random.randint(0, 600), 30, "gold")

save("my_random_art.png")   # also saves your picture as a file!

# Challenge: draw random squares or triangles instead of circles.
