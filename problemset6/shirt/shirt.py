import os
import sys
from PIL import Image, ImageOps

filetype = ['.jpeg', '.jpg', '.png']
def checkFormat(name):
    valid = False
    try:
        fileName, format = os.path.splitext(name)
        format = format.lower()
        if format in filetype:
            valid = True
    except ValueError:
        return valid, (0,0)

    return valid, (fileName, format)

def checkArg():
    extractFile = sys.argv[1:]

    if (countFile := len(extractFile)) != 2:
        if countFile > 2:
            sys.exit('Too many command-line arguments')
        else:
            sys.exit('Too few command-line arguments')

    before = extractFile[0]
    after = extractFile[1]
    formatBefore, beforeFile = checkFormat(before)
    formatAfter, afterFile = checkFormat(after)

    if not formatBefore or beforeFile == (0,0):
        sys.exit('Invalid Input')

    if not formatAfter or afterFile == (0,0):
        sys.exit('Invalid Output')

    if beforeFile[1] != afterFile[1]:
        sys.exit('Input and output have different extensions')

    return extractFile

def main():
    before, after = checkArg()

    try:
        beforeImage = Image.open(before)
    except FileNotFoundError:
        sys.exit('Input does not exist')

    shirt = Image.open('shirt.png')
    size = shirt.size

    muppet = ImageOps.fit(beforeImage, size)
    muppet.paste(shirt, shirt)
    muppet.save(after)

if __name__ == '__main__':
    main()