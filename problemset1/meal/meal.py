def main():
    time = input("Time: ")
    front = float(time[0:time.find(":")])
    back = float(time[time.find(":") + 1 : len(time)])
    if front > 12:
        front = front - 12
    converted = front + (back / 60)
    if converted >= 7 and converted <= 8:
        meal = "breakfast "
    elif converted >= 0 and converted <= 1:
         meal = "lunch "
    elif converted >= 6 and converted <= 7:
        meal = "dinner "
    else:
        meal = ""
    print(meal + "time")

main()