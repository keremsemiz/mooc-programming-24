# Write your solution here
number = float(input("Please type in a number:"))
decimal = number - int(number)
integer = number - decimal

print(f"Integer part: {integer}")
print(f"Decimal part: {decimal}")