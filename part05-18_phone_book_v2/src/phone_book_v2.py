# Write your solution here
def search(phonebook):
    name = input("name:")
    if name not in phonebook:
        print("no number")
    else:
        for num in phonebook[name]:
            print(num)

def add(phonebook):
    name = input("name: ")
    number = input("number: ")

    if name not in phonebook:
        phonebook[name] = []
    
    phonebook[name].append(number)
    print("ok!")

def main():
    phonebook = {}  
    while True: 
        cmd = int(input("command (1 search, 2 add, 3 quit):"))
        if cmd == 1:
            search(phonebook)
        if cmd == 2:
            add(phonebook)
        if cmd == 3:
            break
    print("quitting...")

main()

