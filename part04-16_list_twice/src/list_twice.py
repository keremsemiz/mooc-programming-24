# Write your solution here
values = []
while True:
    item = int(input("New item: "))
    values.append(item)
    print(f"The list now: {values}")
    print(f"The list in order: {values.sort()}")

    if item == 0:
        print("Bye!")
        break