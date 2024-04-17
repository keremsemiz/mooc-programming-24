# Write your solution here
string = input("Please type in a string:")
strlength = len(string)
missingspace = 20 - strlength
star = ""

if strlength <= 20:
    for i in range(missingspace):
        star += "*"
    print(f"{star}", end="")
    print(string)

