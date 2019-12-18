import sys

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from table import elements

image_size = 100
font_path = "/System/Library/Fonts/Supplemental/"
name_font_size = 12
atomic_font_size = 15
symbol_font_size = 30
mass_font_size = 10


def draw_element(name, atomic, symbol, mass) -> Image:
    """
    Draw a periodic element.

    :param name: name of the element.
    :param atomic: atomic number
    :param symbol: chemical symbol
    :param mass: relative atomic mass
    :return: an Image
    """
    image = Image.new("RGB", (image_size, image_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # draw shape
    shape = [(2, 2), (image_size - 2, image_size - 2)]
    draw.rectangle(shape, fill="#ffff33", outline="black")

    # draw name
    font = ImageFont.truetype(font_path + "Arial Narrow.ttf", name_font_size)
    text_size = draw.textsize(name, font=font)
    x = (image_size - text_size[0]) / 2
    y = 5
    draw.text((x, y), name, (0, 0, 0), font=font)

    # draw atomic
    font = ImageFont.truetype(font_path + "Arial Narrow.ttf", atomic_font_size)
    text_size = draw.textsize(atomic, font=font)
    x = (image_size - text_size[0]) / 2
    y = 20
    draw.text((x, y), atomic, (0, 0, 0), font=font)

    # draw symbol
    font = ImageFont.truetype(font_path + "Papyrus.ttc", symbol_font_size)
    text_size = draw.textsize(symbol, font=font)
    x = (image_size - text_size[0]) / 2
    y = (image_size - text_size[1]) / 2
    draw.text((x, y), symbol, (0, 0, 0), font=font)

    # draw mass
    font = ImageFont.truetype(font_path + "Arial Narrow.ttf", mass_font_size)
    text_size = draw.textsize(mass, font=font)
    x = (image_size - text_size[0]) / 2
    y = image_size - 15
    draw.text((x, y), mass, (0, 0, 0), font=font)

    return image


def draw_text(text) -> Image:
    """
    Draw a text.

    :param text: text to draw
    :return: an Image
    """
    image = Image.new("RGB", (image_size, image_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    shape = [(2, 2), (image_size - 2, image_size - 2)]
    draw.rectangle(shape, fill="#ffff33", outline="black")

    font = ImageFont.truetype(font_path + "Papyrus.ttc", symbol_font_size)
    text_size = draw.textsize(text, font=font)
    x = (image_size - text_size[0]) / 2
    y = (image_size - text_size[1]) / 2
    draw.text((x, y), text, (0, 0, 0), font=font)

    return image


def draw_word(word) -> Image:
    """
    Draw a word.

    :param word: word to draw.
    :return: an Image
    """
    pictures = list()
    size = (0, 0)
    for element in word:
        if element in elements:
            name = elements[element]["name"]
            atomic = str(elements[element]["atomic"])
            mass = str(elements[element]["mass"])
            image = draw_element(name, atomic, element, mass)
        else:
            image = draw_text(element)
        pictures.append(image)
        size = (size[0] + image.size[0], max(size[1], image.size[1]))

    return Image.fromarray(np.hstack(pictures))


def main():
    image = draw_word(["Ni", "Co", "La", "S"])
    image.save("nicolas.jpg")
    image.show()
    image = draw_word(["E", "V", "E"])
    image.save("eve.jpg")
    image.show()
    image = draw_word(["Te", "O"])
    image.save("teo.jpg")
    image.show()
    image = draw_word(["C", "H", "R", "Y", "S", "Te", "L", "E"])
    image.save("chrystele.jpg")
    image.show()


if __name__ == '__main__':
    sys.exit(main())
