from random import randint

import pyperclip


def jokeify():
    text = pyperclip.paste()
    upcounter = 0
    out = ""
    for char in text:
        if randint(0, 1) and upcounter < 2:
            out += char.upper()
            upcounter += 1
            continue

        out += char.lower()
        upcounter = 0

    pyperclip.copy(out)
