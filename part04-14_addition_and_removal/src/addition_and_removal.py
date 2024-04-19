# Write your solution here
values = []
val = 1
while True:
    print(f"The list is now {values}")
    choice = input("a(d)d, (r)emove or e(x)it:")
    if choice == "x":
        print("Bye!")
        break
    elif choice == "d":
        values.append(val)
        val += 1
    elif choice == "r":
        values.pop()
        val -= 1