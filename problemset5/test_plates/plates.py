def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    txt = ""
    for i in s:
        if int(i.isnumeric()):
            txt = txt + str(i)

    if txt != '':
        if txt[0] == "0":
            first_num = False
        else:
            first_num = True
        i = 1
        while i <= len(txt):
            if (s.find(txt) + i) < len(s):
                if s[s.find(txt) + 1].isalpha():
                    character = False
            else:
                character = True
            i +=1
    else:
        first_num = True
        character = True

    if s[0:2].isalpha() and first_num and (len(s) <= 6) and (len(s) >= 2) and character:
        return True
    else:
        return False

if __name__ == '__main__':
    main()