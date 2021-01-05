import math
import cairo
import random
import numpy as np

# GLOBAL VARIABLES
WIDTH, HEIGHT = 3000, 5000
N_STARS = 8000


def a_planet(output_path):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

    # BACKGROUND GRADIENT COLOR
    background = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    background.add_color_stop_rgba(1, 0.15, 0.15, 0.2, 1)
    background.add_color_stop_rgba(0, 0, 0, 0, 1)
    ctx.rectangle(0, 0, 1, 1)
    ctx.set_source(background)
    ctx.fill()

    ctx.scale(1, WIDTH/HEIGHT)

    # DRAWING THE STARS
    for i in range(N_STARS):
        random_x = random.uniform(0, 1)
        random_y = random.uniform(0, 2)
        random_r = random.gauss(0.00005, 0.0005)
        ctx.arc(random_x, random_y, random_r, 0, math.pi * 2)
        ctx.set_source_rgb(1, 1, 1)
        ctx.fill()

    # DRAWING THE PLANET
    ctx.translate(0.5, 0.6)  # Changing the current transformation matrix
    ctx.move_to(0, 0)
    ctx.arc(0, 0, 0.3, 0, math.pi*2)
    ctx.translate(-0.5, -0.3)
    planet_gradient = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
    random_r = random.gauss(0.3, 0.1)
    random_g = random.gauss(0.3, 0.1)
    random_b = random.gauss(0.3, 0.1)
    i_max = np.argmax(np.array([random_r, random_g, random_b]))
    if i_max == 0:
        planet_gradient.add_color_stop_rgb(0.6, 0.2, 0.15, 0.15)
    elif i_max == 1:
        planet_gradient.add_color_stop_rgb(0.6, 0.15, 0.2, 0.15)
    else:
        planet_gradient.add_color_stop_rgb(0.6, 0.15, 0.15, 0.2)
    planet_gradient.add_color_stop_rgb(0.1, random_r, random_g, random_b)
    ctx.set_source(planet_gradient)
    ctx.fill()

    # ADD TEXT
    text = 'life is but a dream'
    ctx.select_font_face('Georgia', cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(0.02)

    ctx.move_to(0.5, 0.5)
    random_r = random.uniform(0.6, 1)
    random_g = random.uniform(0.6, 1)
    random_b = random.uniform(0.6, 1)
    ctx.set_source_rgb(1, 1, 1)
    ctx.show_text(text)

    surface.write_to_png(output_path)  # Output to PNG


if __name__ == "__main__":
    for i in range(10):
        a_planet('a_planet_' + str(i) + '.png')
