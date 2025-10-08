import sys

extractFile = sys.argv[1:]
name = ' '.join(extractFile)

if (countFile := len(extractFile)) != 1:
    if countFile > 1:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')

try:
    with open(name, mode = 'r') as file:
        if not name.endswith('.py'):
            sys.exit('Not a Python file')

        totalLines = 0
        for line in file:
            line = line.strip()
            if line.startswith('#') or line == '':
                pass
            else:
                totalLines += 1
except FileNotFoundError:
    sys.exit('File does not exist')

print(totalLines)