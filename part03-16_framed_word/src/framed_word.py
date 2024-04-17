# Write your solution here
word = input("Word:")
wordlength = len(word)
leftspace = (28 - wordlength) // 2
rightspace = (28 - wordlength) // 2
if wordlength % 2 != 0:
    leftspace += 1
    rightspace += 0
leftrealspace = ""
rightrealspace = ""
for i in range(leftspace):
    leftrealspace += " "
for i in range(rightspace):
    rightrealspace += " "

print("******************************")
print(f"*{leftrealspace}{word}{rightrealspace}*")
print("******************************")
