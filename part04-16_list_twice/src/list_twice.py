# Write your solution here
values = []
while True:
    item = int(input("New item:"))
    if item == 0:
        print("Bye!")
        break
    
    values.append(item)
    print(f"The list now: {values}")
    sortedvals = sorted(values)
    print(f"The list in order: {sortedvals}")