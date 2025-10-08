def main():
    while True:
        date = input('Date: ').strip()
        converted = convertToISO(date)
        if converted == -1:
            continue
        elif converted != None:
            year, month, day = converted
            print(f'{year}-{month:02d}-{day:02d}')
            break


M = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def convertToISO(date):
    valid = True
    try:
        if '/' in date:
            date = date.split('/')
            month, day, year = date

            for i in [month, day, year]:
                if not i.isdigit():
                    valid = False
                    break

            month, day, year = map(int, [month, day, year])

        elif ',' in date:
            date = date.replace(',', '')
            date = date.split()
            month, day, year = date
            if (month not in M) or (day in M):
                print('block')
                valid = False

            if valid:
                month = M.index(month) + 1
                month, day, year = map(int, [month, day, year])

        else:
            return -1

        if not valid:
            return -1

        if day > 31 or month > 12:
            return -1

        reconstructed = [year, month, day]
        return reconstructed

    except (ValueError):
        return -1

main()