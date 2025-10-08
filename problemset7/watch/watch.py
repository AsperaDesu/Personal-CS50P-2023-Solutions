import re

def main():
    print(parse(input('HTML: ')))

def parse(s : str):
    if (matches:= re.search(r'((?:http)(?:s)?:\/\/(?:www.)?youtube\.com\/embed\/(.+?))"', s)):
        url = matches.groups()[1]
        new = f'https://youtu.be/{url}'
        return new

    else:
        return None

if __name__ == '__main__':
    main()