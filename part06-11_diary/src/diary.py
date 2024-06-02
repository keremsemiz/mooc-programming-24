# Write your solution here
def readFile(filename):
    with open(filename) as diary:
        print("Entries: ")
        for line in diary:
            print(line.replace('\n', ''))
        
        diary.close()

def writeFile(filename, entry):
    with open(filename, 'a') as diary:
        diary.write(f"{entry}\n")
        
        diary.close()

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    inpt = int(input("Function: "))
    if inpt == 0:
        print("Bye now!")
        break
    elif inpt == 1:
        entry = input("Diary entry: ")
        writeFile("diary.txt", entry)
        print("Diary saved")
    elif inpt == 2:
        readFile("diary.txt")