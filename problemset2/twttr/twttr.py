twitter = input("Input: ")

output = ""
for word in twitter:
    if word.lower() in "aiueo":
        continue
    else:
        output = output + word

print(f"Output: {output}")