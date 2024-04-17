# Write your solution here
word = input("Please type in a string:")
length = len(word)
num = 0
for i in range(length):
    num += 1
    print(word[:num])