import os
import textwrap
from pathlib import Path

import pyperclip
from PIL import Image, ImageDraw, ImageFont, ImageGrab

from shortcuts import helpers
from shortcuts.logger import log


def edit_text(base_image: Image) -> Image:
    path = Path(__file__).parent

    # Get the text and copy it on the image
    text = f'"{pyperclip.paste()}"'
    wrapped = textwrap.wrap(text, width=40)

    # Select the font
    font_path = os.path.join(path, "fonts", "arial.ttf")
    font = ImageFont.truetype(font_path)

    # Create a draw object
    draw = ImageDraw.Draw(base_image)
    draw.text((50, 15), "\n".join(wrapped), (0, 0, 0), font=font)
    return base_image


def edit_image(base_image: Image, clip_image: Image) -> Image:
    path = Path(__file__).parent

    clip_image = clip_image.convert("RGBA")
    clip_image = clip_image.resize((300, 300))

    # Paste the left guy on the bottom left
    bottom_left = os.path.join(path, "images", "bottom_left.png")
    left_guy = Image.open(bottom_left).convert("RGBA")
    base_image.paste(clip_image, (50, 20), clip_image)
    base_image.paste(left_guy, (0, 142), left_guy)
    return base_image


def get_image(base_image) -> Image:
    try:
        clip_image = ImageGrab.grabclipboard()
    except Exception as e:
        log(e)
        clip_image = None

    if not clip_image:
        return edit_text(base_image)

    return edit_image(base_image, clip_image)


def soyify():
    path = Path(__file__).parent

    # Get the soyjack image
    image_path = os.path.join(path, "images", "soy.png")
    image = Image.open(image_path).convert("RGBA")

    # Check if there is an image in the clipboard
    image = get_image(image)
    helpers.to_clipboard(image)
