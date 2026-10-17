# Lesson 5: Animation - make things move!
# The draw function runs 30 times every second. "frame" counts up: 0, 1, 2, 3 ...

from drawing import *


def draw(frame):
    background("midnightblue")              # wipe the screen each time

    # a ball moving to the right (and starting again on the left)
    x = (frame * 5) % 800
    circle(x, 200, 40, "orange")

    # a circle that follows your mouse
    circle(mouse_x(), mouse_y(), 20, "hotpink")

    # hold the space bar to draw a big star
    if key_down("space"):
        star(400, 450, 80, "gold")

    text("Move the mouse. Hold SPACE. Press ESC to quit.", 20, 20, "white", 30)


animate(draw)

# Challenge: make the ball go faster. Can you make a second ball go the other way?
