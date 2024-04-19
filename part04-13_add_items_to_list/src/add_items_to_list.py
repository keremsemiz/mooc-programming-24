# Write your solution here
amount = int(input("How many items:"))
i = 0
num = 1
items = []
while i < amount:
    itadd = int(input(f"Item {num}:"))
    items.append(itadd)
    num += 1
    i += 1
print(items)