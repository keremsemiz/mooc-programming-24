# Write your solution here
i = 1
factorial = 1
while True:
    num = int(input("Please type in a number:"))
    if num <= 0:
        print("Thanks and bye!")
        break
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of the number {num} is {factorial}")
    factorial = 1
