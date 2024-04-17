# Write your solution here
studentFood = float(input("How many times a week do you eat at the student cafeteria?"))
studentPrice = float(input("The price of a typical student lunch?"))
groceryPrice = float(input("How muh money do you spend on groceries in a week?"))

daily = (groceryPrice / 7) + ((studentFood * studentPrice)/7)
weekly = groceryPrice + (studentFood * studentPrice)

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")