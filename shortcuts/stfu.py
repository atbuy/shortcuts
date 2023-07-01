import os
from pathlib import Path

from PIL import Image, ImageGrab

from shortcuts import helpers
from shortcuts.logger import log


def shut_up():
    # Get current working directory (cwd)
    path = Path(__file__).parent

    # Get the stfu image
    image_path = os.path.join(path, "images", "shutthefuckup.png")
    image = Image.open(image_path)

    # Check if there is an image in the clipboard
    clip_image = ImageGrab.grabclipboard()
    if not clip_image:
        log("Could not find image in clipboard.")
        return

    clip_image = clip_image.resize((680, 450))
    image.paste(clip_image)

    helpers.to_clipboard(image)
