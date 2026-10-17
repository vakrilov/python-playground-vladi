"""
drawing.py - a tiny helper that makes drawing with Python easy.

You don't need to change this file. Just put this line at the top of your program:

    from drawing import *

The screen works like a grid of pixels:
    - (0, 0) is the TOP-LEFT corner
    - x gets bigger as you go RIGHT
    - y gets bigger as you go DOWN
"""

import atexit
import math
import os
import random
import sys

os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
import pygame

_screen = None
_clock = None
_fonts = {}
_shown = False
_crashed = False


# ---------------------------------------------------------------- window

def window(width=800, height=600, title="My Drawing"):
    """Open a drawing window. If you skip this, you get an 800 x 600 window."""
    global _screen, _clock
    pygame.init()
    _screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    _clock = pygame.time.Clock()
    _screen.fill("white")


def _get_screen():
    if _screen is None:
        window()
    return _screen


def screen_width():
    return _get_screen().get_width()


def screen_height():
    return _get_screen().get_height()


# ---------------------------------------------------------------- colors

def _color(c):
    try:
        return pygame.Color(c)
    except (ValueError, TypeError):
        raise ValueError(
            f"I don't know the color {c!r}. "
            "Try a name like 'red', 'skyblue', 'gold' or numbers like (255, 0, 0)."
        ) from None


def random_color():
    """Get a random bright color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def background(color="white"):
    """Paint the whole screen one color (this also wipes everything off)."""
    _get_screen().fill(_color(color))


# ---------------------------------------------------------------- shapes
# outline=0 means "filled in". outline=3 means "just the edge, 3 pixels thick".

def circle(x, y, radius, color="black", outline=0):
    """A circle. (x, y) is the CENTER."""
    pygame.draw.circle(_get_screen(), _color(color), (x, y), radius, outline)


def rectangle(x, y, width, height, color="black", outline=0):
    """A rectangle. (x, y) is the TOP-LEFT corner."""
    pygame.draw.rect(_get_screen(), _color(color), (x, y, width, height), outline)


def square(x, y, size, color="black", outline=0):
    """A square. (x, y) is the TOP-LEFT corner."""
    rectangle(x, y, size, size, color, outline)


def ellipse(x, y, width, height, color="black", outline=0):
    """An oval that fits in a box. (x, y) is the TOP-LEFT of the box."""
    pygame.draw.ellipse(_get_screen(), _color(color), (x, y, width, height), outline)


def triangle(x1, y1, x2, y2, x3, y3, color="black", outline=0):
    """A triangle with corners at (x1, y1), (x2, y2) and (x3, y3)."""
    polygon([(x1, y1), (x2, y2), (x3, y3)], color, outline)


def polygon(points, color="black", outline=0):
    """Any shape you like. points is a list of corners: [(x, y), (x, y), ...]"""
    pygame.draw.polygon(_get_screen(), _color(color), points, outline)


def star(x, y, size, color="gold", points=5, outline=0):
    """A star. (x, y) is the CENTER."""
    corners = []
    for i in range(points * 2):
        r = size if i % 2 == 0 else size * 0.45
        angle = math.pi * i / points - math.pi / 2
        corners.append((x + r * math.cos(angle), y + r * math.sin(angle)))
    polygon(corners, color, outline)


def line(x1, y1, x2, y2, color="black", thickness=2):
    """A straight line from (x1, y1) to (x2, y2)."""
    pygame.draw.line(_get_screen(), _color(color), (x1, y1), (x2, y2), thickness)


def text(message, x, y, color="black", size=32):
    """Write words on the screen. (x, y) is the TOP-LEFT of the text."""
    _get_screen()
    if size not in _fonts:
        _fonts[size] = pygame.font.Font(None, size)
    picture = _fonts[size].render(str(message), True, _color(color))
    _screen.blit(picture, (x, y))


# ---------------------------------------------------------------- mouse & keyboard

def mouse_x():
    return pygame.mouse.get_pos()[0]


def mouse_y():
    return pygame.mouse.get_pos()[1]


def mouse_down():
    """True while the mouse button is held down."""
    return pygame.mouse.get_pressed()[0]


def key_down(name):
    """True while a key is held. Examples: 'left', 'right', 'up', 'down', 'space', 'a'."""
    return pygame.key.get_pressed()[pygame.key.key_code(name)]


# ---------------------------------------------------------------- showing it

def save(filename="my_picture.png"):
    """Save what's on the screen as a picture file."""
    pygame.image.save(_get_screen(), filename)


def _window_closed():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True
    return False


def show():
    """Show your drawing and keep the window open until you close it."""
    global _shown
    _shown = True
    _get_screen()
    while not _window_closed():
        pygame.display.flip()
        _clock.tick(30)
    pygame.quit()


def animate(draw, fps=30):
    """Make things move! Calls your draw(frame) function again and again.

    frame starts at 0 and goes up by 1 every time, so you can use it to move things.
    """
    global _shown
    _shown = True
    _get_screen()
    frame = 0
    while not _window_closed():
        draw(frame)
        pygame.display.flip()
        _clock.tick(fps)
        frame += 1
    pygame.quit()


# If you forget to call show(), we show the drawing for you at the end.
def _auto_show():
    if _screen is not None and not _shown and not _crashed:
        show()


def _note_crash(*args):
    global _crashed
    _crashed = True
    sys.__excepthook__(*args)


sys.excepthook = _note_crash
atexit.register(_auto_show)
