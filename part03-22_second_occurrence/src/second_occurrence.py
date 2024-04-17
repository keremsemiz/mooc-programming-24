# Write your solution here
word = input("Please type in a string:")
substring = input("Please type in a substring:")
i = 0
loc1 = word.find(substring)
loc2 = -1

if loc1 != -1:
    loc2 = word.find(substring, loc1 + len(substring))

if loc2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {loc2}.")