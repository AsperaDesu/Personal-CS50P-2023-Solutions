import sys
from datetime import date
import re
import inflect

def main():
    engine = inflect.engine()
    birth = input('Date of Birth: ')
    birth = checkFormat(birth)

    if birth is not None:
        year, month, day = birth
    else:
        sys.exit('Invalid date')

    dateBirth = date(int(year), int(month), int(day))
    currentDay = date.today()

    displacement = currentDay - dateBirth
    minutes = getMinutes(displacement)

    print((engine.number_to_words(minutes, andword = '')).capitalize(), 'minutes')


def checkFormat(bdate : str):
    if extract := re.search(r'^([0-9]{4})-([0-9]{2})-([0-9]{2})$', bdate):
         return extract.groups()


def getMinutes(days : int):
    return days.days * (24 * 60)


if __name__ == '__main__':
    main()