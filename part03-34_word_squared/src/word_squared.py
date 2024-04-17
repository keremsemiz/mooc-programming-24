# Write your solution here
def squared(text, length):
    letters = []
    x = 0
    for j in text:
        letters += j

    for i in range(length):
        for z in range(length):
            j = letters[x]
            print(j, end="")
            x += 1
            if x == len(letters):
                x = 0
        print()
if __name__ == "__main__":
    squared("abc", 5)