import re

def main():
    print(convert(input("Hours: ")))

def convert(s:str):
    if (matches:= re.search(r'([0-9]*)(?:\:)?([0-9]*) (AM|PM) to ([0-9]*)(?:\:)?([0-9]*) (AM|PM)', s)):
        timeList = matches.groups()
        hours1, hours2 = timeList[0], timeList[3]
        minutes1, minutes2 = timeList[1], timeList[4]
        phase1, phase2 = timeList[2], timeList[5]

        for time in (hours := list(map(lambda x: int(x), [hours1, hours2]))):
            if time > 12 or time < 0:
                raise ValueError

        minutes = []
        for time in [minutes1, minutes2]:
            if time == '':
                time = 0
            else:
                time = int(time)
                if time > 59 or time < 0:
                    raise ValueError
            minutes.append(time)

        newHour1, newHour2 = convertHours(hours[0], phase1), convertHours(hours[1], phase2)
        return f'{newHour1:02d}:{minutes[0]:02d} to {newHour2:02d}:{minutes[1]:02d}'
    else:
        raise ValueError

def convertHours(hour:int, phase:str):
    hour = int(hour)
    if phase == 'PM':
        if hour == 12:
            hour = 12
        else:
            hour += 12
    else:
        if hour == 12:
            hour = 0 
    return hour

if __name__ == '__main__':
    main()

# program has run correctly. tasks left are the following
# 1. ignore minutes if there aren't any in the first place. eg: 9 AM
# 2. find a way to change the ignored minutes to 00. eg : 9 AM -> 9:00
# 3. catch wrong input of hours / minutes with raise valuerror
# 4. catch '-' as valuerror
