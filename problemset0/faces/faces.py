word = input()

def convert(word : str):
    word = word.replace(':)', '🙂')
    word = word.replace(':(', '🙁')

    return word

print(convert(word))