# Write your solution here
width = int(input("Width:"))
height = int(input("Height:"))
wi = 0
hi = 0

for hi in range(height):
    while wi < width:
        wi += 1
        print("#", end="")
    print()
    wi = 0