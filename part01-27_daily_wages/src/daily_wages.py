# Write your solution here
hourlywage = float(input("Hourly wage:"))
hoursworked = float(input("Hours worked:"))
day = input("Day of the week:")


if day == "Sunday":
    print(f"Daily wages: {2*(hourlywage * hoursworked)} euros")
else:
    print(f"Daily wages: {hourlywage * hoursworked} euros")