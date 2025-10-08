import random
from pyfiglet import Figlet as fg
import sys

arguments = sys.argv[1:]
figlet = fg()

def main():
    fig = arg_handling()
    word = input('Input: ')
    print(fig.renderText(word))

def arg_handling():
    if arguments:
        if (arguments[0] in ['-f', '--font']) and (len(arguments) > 1):
            fontz = arguments[1]
        else:
            sys.exit('Invalid usage')
    else:
        fontz = random.choice(figlet.getFonts())

    try:
        figlet.setFont(font = fontz)
    except Exception:
        sys.exit('Invalid usage')

    return figlet


if __name__ == '__main__':
    main()
