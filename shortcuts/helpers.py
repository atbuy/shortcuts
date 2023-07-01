import os
import sys
import uuid
from io import BytesIO

from PIL import Image

if sys.platform == "win32":
    import win32clipboard
elif sys.platform in ("linux", "darwin"):
    TEMP_DIR = "/tmp/stfu"


def to_clipboard(image: Image) -> None:
    if sys.platform == "win32":
        obj = BytesIO()
        image.convert("RGB").save(obj, "BMP")
        data = obj.getvalue()[14:]
        obj.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        return

    if sys.platform in ("linux", "darwin"):
        # Save the image to a temporary file
        if not os.path.exists(TEMP_DIR):
            os.mkdir(TEMP_DIR)

        filename = uuid.uuid4().hex
        image.save(f"{TEMP_DIR}/{filename}.png")

        # Copy the image to the clipboard
        cat = f"cat {TEMP_DIR}/{filename}.png"
        xclip = "xclip -selection clipboard -t image/png"
        os.system(f"{cat} | {xclip}")
        return
