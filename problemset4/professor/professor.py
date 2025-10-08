import random

def get_level():
    lvl = ""

    while not lvl.isnumeric() or int(lvl) < 1 or int(lvl) > 3:
        lvl = input("Level: ")

    return int(lvl)

def get_int(prompt :str, EEE = True, limit = None):
    try:
        num = int(input(prompt))
        valid = True
        if num <= 0:
            valid = False
        if limit is not None:
            if num > limit:
                valid = False

        if not valid:
            return None

        return num

    except ValueError:
        if EEE:
            print('EEE')
            return None


def init_level(level : int):
    match level:
        case 1:
            level = [0, 9]
        case 2:
            level = [10, 99]
        case 3:
            level = [100, 999]

    score = 0
    for i in range(10):
        first = random.randint(level[0], level[1])
        second = random.randint(level[0], level[1])
        answer = first + second
        attempts = 0
        user = 'asdf'

        while attempts < 3 and (result := answer != user):
            attempts += 1
            user = get_int(f'{first} + {second} = ')

            if result:
                print('EEE')


        if result:
            print(f'{first} + {second} = {answer}')
        else:
            score += 1

    return score


def main():
    level = get_level()
    score = init_level(level)

    print(f'Score: {score}')


if __name__ == '__main__':
    main()
