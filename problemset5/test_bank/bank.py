def main():
    greet1 = input("Greeting: ")
    output = value(greet1)
    print(f"${output}")

def value(greet1 : str):
    greet = greet1.lower().strip()

    if greet.startswith("h"):
        output = 20
        if greet.startswith("hello"):
            output = 0
    else:
        output = 100

    return output



if __name__ == '__main__':
    main()