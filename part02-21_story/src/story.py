# Write your solution here
words = ("")
lastword = None
word = input("Please type in a word:")
if word != "end":
    while True:
        words += word + " "
        lastword = word
        word = input("Please type in a word:")
        if word == "end":
            print(f"{words}")
            break
        elif word == lastword:
            print(f"{words}")
            break