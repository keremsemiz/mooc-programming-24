# Write your solution here
#number >= 5 and number <= 8

age = int(input("What is your age?"))
if age >= 5 and age <= 200:
    print(f"Ok, you're {age} years old")
if age >= 0 and age <= 4:
    print("I suspect you can't write quite yet")
elif age <= -1:
    print("That must be a mistake")