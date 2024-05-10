# Write your solution here
phonebook = {}

while True:
    cmd = int(input("command (1 search, 2 add, 3 quit):"))
    if cmd == 3:
        print("quitting...")
        break
    name = str(input("name:"))
    if cmd == 2:
        number = input("number:")
        print("ok!")


    if cmd == 2:
        phonebook[name] = number
    elif cmd == 1:
        if name not in phonebook:
            print("no number")
        else:
            print(phonebook[name])