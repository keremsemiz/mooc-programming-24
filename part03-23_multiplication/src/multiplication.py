# Write your solution here
number = int(input("Please type in a number:"))
num1 = 1

while num1 <= number:
    num2 = 1
    while num2 <= number:
        print(f"{num1} x {num2} = {num1*num2}")
        num2 += 1
    num1 += 1

