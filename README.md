# shortcuts

A python script to create keybinds for quick edits to input from your clipboard.

## Installation

Clone the repository and install the dependencies:

```bash
pip install -e .
```

## Usage

### Windows

If you are on windows you can just double click the run.pyw file,which will open up the script in a background process, with no terminal.

### Linux

On linux you can use the following command to run the script from the project's root directory:

```bash
sudo python3 run.pyw
```

You can also create a startup command and give it root permissions without requiring a password. To do this, open up the terminal and type:

```bash
sudo visudo
```

Then add an entry with this line as an example:

```bash
user ALL = NOPASSWD: /home/user/.virtualenvs/shortcuts/bin/python /home/user/path/to/shortcuts/run.pyw
```

After that you can restart your computer and the script will run on startup.
