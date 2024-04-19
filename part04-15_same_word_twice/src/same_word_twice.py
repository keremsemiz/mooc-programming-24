# Write your solution here
words = []
i = 0
while True:
    word = input("Word:")
    words.append(word)
    if words.count(word) == 2:
        print(f"You typed in {len(words) - 1} different words")
        break
    i += 1