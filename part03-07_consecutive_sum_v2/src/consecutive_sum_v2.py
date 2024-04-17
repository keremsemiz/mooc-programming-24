# Write your solution here
limit = int(input("Limit:"))
i = 1
num = 1
calc = "1"
while i < limit:
    num += 1
    i += num
    calc += f" + {num}"
    calculation = "The consecutive sum: "
    calculation += f"{calc} = {i}"

print(calculation)
