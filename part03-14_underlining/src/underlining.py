# Write your solution here
while True:
    print()
    string = input("Please type in a string:")
    strlength = len(string)
    print(string)
    for i in range(strlength):
        print("-", end="")
    
    if strlength <= 0:
        break