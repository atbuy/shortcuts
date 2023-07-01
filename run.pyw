import keyboard

from shortcuts import soy, stfu, joke, pepethink
from shortcuts.helpers import setup_logger

setup_logger()

# Setup hotkeys
keyboard.add_hotkey("ctrl+shift+1", soy.soyify)
keyboard.add_hotkey("ctrl+shift+2", stfu.shut_up)
keyboard.add_hotkey("ctrl+shift+3", joke.jokeify)
keyboard.add_hotkey("ctrl+shift+4", pepethink.pepethink)

# Blocking wait for hotkeys
keyboard.wait()
