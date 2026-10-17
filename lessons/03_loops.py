# Lesson 3: Loops - let the computer repeat things for you.

from drawing import *

background("black")

# A row of 10 circles. "for i in range(10)" repeats 10 times, with i = 0, 1, 2 ... 9
for i in range(10):
    circle(40 + i * 80, 100, 30, "orange")

# Circles that get bigger
for i in range(8):
    circle(60 + i * 95, 300, 5 + i * 6, "cyan", outline=3)

# A rainbow of stripes
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(6):
    rectangle(100 + i * 100, 450, 100, 100, colors[i])

# Challenge: change range(10) to range(20). What happens? Can you fix it so they fit?
