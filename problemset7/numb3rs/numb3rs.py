import re

def main():
    print(validate(input('IPv4 Address: ')))

def validate(ip):
    if re.search(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$', ip):
        listMatches = ip.split('.')
        for num in map(lambda x: int(x), listMatches):
            if num > 255 or num < 0:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    main()