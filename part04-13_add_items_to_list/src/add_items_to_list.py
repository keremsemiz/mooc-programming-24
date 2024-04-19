# Write your solution here
amount = int(input("How many items:"))
i = 0
num = 1
items = []
while i < amount:
    itemstoadd = int(input(f"Item {num}:"))
    items.append(itemstoadd)
    num += 1
    i += 1
print(items)