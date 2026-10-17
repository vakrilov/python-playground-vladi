# Python Playground 🎨

Learn Python by drawing pictures and making things move!

## How to run a program

Open this folder in VS Code, open any `.py` file, and press the ▶ button (top right).

Or in the terminal:

```
.venv/bin/python lessons/01_first_shapes.py
```

Close the window (or press **ESC**) when you're done.

## Lessons

Do them in order. Each one ends with a **Challenge**.

1. `lessons/01_first_shapes.py`: circles, rectangles, triangles, text
2. `lessons/02_house.py`: build a picture out of shapes
3. `lessons/03_loops.py`: let the computer repeat things
4. `lessons/04_random_art.py`: random pictures (saved as a PNG file too)
5. `lessons/05_animation.py`: moving things, mouse and keyboard

Put your own programs in `my_programs/`.

## The screen

```
(0,0) ───────── x gets bigger ──────▶ (800,0)
  │
  │  y gets bigger
  ▼
(0,600)
```

## Everything you can draw

Start every program with `from drawing import *`.

| Command | What it does |
|---|---|
| `background("skyblue")` | paint the whole screen |
| `circle(x, y, radius, "red")` | circle, (x, y) is the center |
| `rectangle(x, y, width, height, "blue")` | rectangle, (x, y) is the top-left corner |
| `square(x, y, size, "green")` | square |
| `ellipse(x, y, width, height, "pink")` | oval |
| `triangle(x1, y1, x2, y2, x3, y3, "orange")` | triangle with 3 corners |
| `polygon([(x, y), (x, y), ...], "purple")` | any shape |
| `star(x, y, size, "gold")` | star |
| `line(x1, y1, x2, y2, "black", thickness)` | line |
| `text("Hi!", x, y, "black", size)` | words |
| `random_color()` | a surprise color |
| `save("picture.png")` | save your drawing |
| `window(1000, 700, "Title")` | change the window size (call it first) |

Add `outline=3` to any shape to draw only its edge.

**Colors:** names like `"red"`, `"skyblue"`, `"gold"`, `"hotpink"`, `"forestgreen"`,
or mix your own with numbers `(red, green, blue)` from 0 to 255, e.g. `(255, 128, 0)`.

**Animation:** write a `draw(frame)` function and call `animate(draw)`.
Inside, you can use `mouse_x()`, `mouse_y()`, `mouse_down()`, `key_down("space")`.

---

### For grown-ups: setup on a new computer

Needs [uv](https://docs.astral.sh/uv/):

```
uv venv --python 3.12
uv pip install -e .
```

`drawing.py` is a small wrapper around [pygame](https://www.pygame.org). When he outgrows it,
he can use pygame directly.
