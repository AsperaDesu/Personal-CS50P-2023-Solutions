import csv
import sys

extractFile = sys.argv[1:]

if (countFile := len(extractFile)) != 2:
    if countFile > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')

before = extractFile[0]
after = extractFile[1]

new = []

with open(after, 'w') as write:
    writer = csv.DictWriter(write, fieldnames = ['first', 'last', 'house'])
    writer.writeheader()
    try:
        with open(before) as file:
            if not before.endswith('.csv'):
                sys.exit('Not a CSV File')
            reader = csv.DictReader(file)

            for row in reader:
                last, first = row['name'].split(',')
                last = last.strip()
                first = first.strip()

                writer.writerow({'first' : first,
                                'last' : last,
                                'house' : row['house']}
                                )
    except FileNotFoundError:
        sys.exit('Could not read {before}')