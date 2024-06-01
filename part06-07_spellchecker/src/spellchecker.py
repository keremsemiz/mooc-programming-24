# write your solution here
with open("wordlist.txt") as wordlist:
    wordlistASLIST = []
    for line in wordlist:
        line = line.strip()
        wordlistASLIST.append(line.lower())

text = input("Write text: ")
textnospace = text.split(' ')
final = ''

for text_word in textnospace:
    if text_word.lower() in wordlistASLIST:
        final += text_word + " "
    else:
        final += "*" + text_word + "* "

print(final.strip())
