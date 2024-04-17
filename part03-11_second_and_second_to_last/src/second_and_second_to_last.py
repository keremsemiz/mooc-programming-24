# Write your solution here
input_string = input("Please type in a string:")
index = 0
while index <= len(input_string):
    index = len(input_string) - 2
    last = input_string[index]
    
    newindex = len(input_string) - len(input_string) + 1
    first = input_string[newindex]

    if first != last:
        print("The second and the second to last characters are different")
        break
    else:
        print(f"The second and the second to last characters are {first}")
        break