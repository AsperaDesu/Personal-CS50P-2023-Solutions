import math

def main():
    again = -1
    while again == -1:
        x = input("Fraction: ")
        again = convert(x)
    y = gauge(again)
    print(y)

def convert(ask):
    try:
        ask = ask.strip().split('/')
        for i in range(0, len(ask)):
            ask[i] = int(ask[i])
        if ask[0] > ask[1]:
            return -1
        else:
            try:
                x, y = ask
                percent = round((float(x) / float(y)) * 100)
                return percent
            except ZeroDivisionError:
                return 1
    except (ValueError, ZeroDivisionError, IndexError):
        raise

def gauge(percent):
    if percent >= 99:
        return 'F'
    elif percent <= 1:
        return 'E'
    else:
        return str(int(percent)) + '%'

if __name__ == '__main__':
    main()