camel = input("camelCase: ")
text = ""

for word in camel:
    if word == word.upper():
        text = text + "_" + word.lower()
    else:
        text = text + word

print(text)