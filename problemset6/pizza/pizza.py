from tabulate import tabulate
import csv
import sys

extractFile = sys.argv[1:]
name = ' '.join(extractFile)

if (countFile := len(extractFile)) != 1:
    if countFile > 1:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')

menu = []

try:
    with open(name) as file:
        if not name.endswith('.csv'):
            sys.exit('Not a CSV File')
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit('File does not exist')

headers = list(menu[0].keys())
values = []
for pizza in menu:
    temp = []
    for key, value in pizza.items():
        temp.append(value)
    values.append(temp)

table = tabulate(values, headers, tablefmt = 'grid')
print(table)