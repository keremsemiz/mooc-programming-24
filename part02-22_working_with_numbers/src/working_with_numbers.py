# Write your solution here
numbersamount = 0
numberssum = 0
numberspositive = 0
numbersnegative = 0

print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number:"))
    if number == 0:
        break
    elif number != 0:
        numbersamount += 1
        numberssum += number
        if number > 0:
            numberspositive += 1
        elif number < 0:
            numbersnegative += 1

numbersmean = float(numberssum / numbersamount)
print(f"Numbers typed in {numbersamount}")
print(f"The sum of the numbers is {numberssum}")
print(f"The mean of the numbers is {numbersmean}")
print(f"Positive numbers {numberspositive}")
print(f"Negative numbers {numbersnegative}")
