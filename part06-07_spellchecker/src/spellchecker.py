# write your solution here
with open("wordlist.txt") as wordlist:
    wordlistASLIST = []
    for line in wordlist:
        line = line.replace("\n", "")
        wordlistASLIST.append(line)
        
    text = input("Write text: ")
    textnospace = text.split(' ')
    final = ''

    for index, word in enumerate(wordlist):
        wordlist[index] = word.lower()

    for text in textnospace:
        if text.lower() in wordlist:
            final += text
        else:
            final += "*" + text + "*"

print(final)