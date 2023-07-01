import textwrap
from pathlib import Path

import pyperclip
from PIL import Image, ImageDraw, ImageFont, ImageGrab

from shortcuts import helpers
from shortcuts.helpers import log


def edit_text(base_image: Image) -> Image:
    """Edit text on pepethink image"""

    path = Path(__file__).parent

    # Get the text and wrap it to fit inside the bubble
    text = f'"{pyperclip.paste()}"'
    wrapped = textwrap.wrap(text, width=30)

    # Select the font
    font_path = str(path.joinpath("fonts", "arial.ttf").absolute())
    font = ImageFont.truetype(font_path, size=30)

    # Create the draw object and write text on image
    draw = ImageDraw.Draw(base_image)
    draw.text((260, 60), "\n".join(wrapped), (0, 0, 0), font=font)
    return base_image


def edit_image(base_image: Image, clip_image: Image) -> Image:
    """Edit image inside the pepethink bubble"""

    path = Path(__file__).parent

    # Resize the image to fit inside the bubble
    clip_image = clip_image.convert("RGBA")
    clip_image = clip_image.resize((500, 400))

    # Paste clip image inside bubble
    top_path = path.joinpath("images", "pepethink_top.png")
    top = Image.open(top_path).convert("RGBA")
    base_image.paste(clip_image, (220, 20), clip_image)
    base_image.paste(top, (0, 0), top)
    return base_image


def get_image(base_image: Image) -> Image:
    """Edit image or text on pepethink image"""

    try:
        clip_image = ImageGrab.grabclipboard()
    except Exception as e:
        clip_image = None
        log(e)

    if not clip_image:
        return edit_text(base_image)

    return edit_image(base_image, clip_image)


def pepethink():
    path = Path(__file__).parent

    # Get the pepethink image
    image_path = path.joinpath("images", "pepethink_base.png")
    image = Image.open(image_path).convert("RGBA")

    # Edit any image or text into the thinking bubble
    image = get_image(image)
    helpers.to_clipboard(image)
