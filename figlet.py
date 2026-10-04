import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# Check command-line arguments
if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")

    font = sys.argv[2]

else:
    sys.exit("Invalid usage")

# Get text
text = input("Input: ")

# Print in selected font
figlet.setFont(font=font)
print(figlet.renderText(text))

