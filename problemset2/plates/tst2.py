s = input("Plates: ")
txt = ""
for i in s:
    if int(i.isnumeric()):
        txt = txt + str(i)

i = 0
while i < len(txt):
    if s[s.find(txt) + i].isalpha():
        print("yes")
    else:
        print("NO")
    i +=1
