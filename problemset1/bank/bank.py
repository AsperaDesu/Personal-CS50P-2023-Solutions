greet1 = input("Greeting: ")
greet = greet1.lower().strip()

if greet.startswith("h"):
    output = 20
    if greet.startswith("hello"):
        output = 0
else:
    output = 100

print(f"${output}")

