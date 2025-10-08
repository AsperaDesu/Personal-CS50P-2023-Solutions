def main():
    twitter = convert(input("Input: "))
    print(f"Output: {twitter}")

def convert(username : str):
    output = ""
    for word in username:
        if word.lower() in "aiueo":
            continue
        else:
            output = output + word
    return output

if __name__ == '__main__':
    main()
