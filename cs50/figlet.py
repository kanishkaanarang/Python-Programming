import sys
import subprocess
import importlib
import random

try:
    pyfiglet = importlib.import_module('pyfiglet')
except ImportError:
    # Attempt to install pyfiglet automatically
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
        pyfiglet = importlib.import_module('pyfiglet')
    except Exception:
        print("Error: required package 'pyfiglet' is not installed and automatic installation failed.")
        print(f"Please install it manually: {sys.executable} -m pip install pyfiglet")
        sys.exit(1)

def get_random_font():
    """ Return a random font from pyfiglet fonts. """
    return random.choice(pyfiglet.FigletFont.getFonts())

def main():
    # Check the command-line arguments
    if len(sys.argv) == 1:
        # No arguments: Use a random font
        font_name = get_random_font()
    elif len(sys.argv) == 3:
        # Two arguments: Check for -f or --font
        if sys.argv[1] in ('-f', '--font'):
            font_name = sys.argv[2]
            # Validate if the font exists
            if font_name not in pyfiglet.FigletFont.getFonts():
                print(f"Error: Font '{font_name}' not found.")
                sys.exit(1)
        else:
            print("Error: Invalid arguments.")
            sys.exit(1)
    else:
        print("Error: Incorrect number of arguments.")
        sys.exit(1)

    # Prompt the user for text input
    text = input("Enter the text to display: ")

    # Create a Figlet font object with the selected font
    figlet = pyfiglet.Figlet(font=font_name)

    # Generate and print the formatted text
    print(figlet.renderText(text))

if __name__ == '__main__':
    main()
