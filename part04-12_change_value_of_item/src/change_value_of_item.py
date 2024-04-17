# Write your solution here
values = [1, 2, 3, 4, 5]
while True:
    ind = int(input("Test"))
    if ind == -1:
        break
    val = int(input("New value:"))
    values[ind] = val
    print(values)