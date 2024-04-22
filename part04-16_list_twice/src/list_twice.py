# Write your solution here
values = []
sortedlist = None
while True:
    item = int(input("New item:"))
    values.append(item)
    print(f"The list now: {values}")
    sortedlist = values.sort()
    print(f"The list in order: {sortedlist}")

    if item == 0:
        print("Bye!")
        break