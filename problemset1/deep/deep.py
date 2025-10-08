answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer2 = answer.strip()

if answer2 == "42" or answer2.lower() == "forty two" or answer2.lower() == "forty-two":
    print("Yes")
else:
    print("No")

