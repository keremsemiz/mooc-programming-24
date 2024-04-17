# Write your solution here
students = int(input("How many students on the course?"))
groupSize = int(input("Desired group size?"))

groupAmount = (students + groupSize -1) // groupSize

print(f"Number of groups formed: {groupAmount}")