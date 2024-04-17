# Write your solution here
word1 = input("Please type in the 1st word:")
word2 = input("Please type in the 2nd word:")

if word1 < word2:
    print(f"{word2} comes alphabetically last")
if word2 < word1:
    print(f"{word1} comes alphabetically last")
if word1 == word2:
    print("You gave the same word twice.")