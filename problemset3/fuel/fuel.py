import math

def main():
    x = get_num("Fraction: ")
    y = get_per(x[0], x[1])
    print(y)

def get_num(prompt):
    while True:
        try:
            ask = input(prompt).split('/')
            for i in range(0, len(ask)):
                ask[i] = int(ask[i])
            if ask[0] > ask[1]:
                continue
            else:
                return ask

        except ZeroDivisionError and ValueError:
            pass

def get_per(x, y):
    percent = round((float(x) / float(y)) * 100)

    if percent >= 99:
        return 'F'
    elif percent <= 1:
        return 'E'
    else:
        return str(int(percent)) + '%'

main()