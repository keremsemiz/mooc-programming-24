# Write your solution here
from random import randint, choice
from string import ascii_letters

def generate_strong_password(length: int, secondArgument: bool, thirdArgument: bool):
    specialChars = "!?=+-()#"
    output = ''
    while len(output) < length:
        if len(output) < length:
            output += choice(ascii_letters.lower())
        if secondArgument and len(output) < length:
            output += str(randint(0, 9))
        if thirdArgument and len(output) < length:
            output += choice(specialChars)
    
    return output

if __name__ == "__main__":
    print(generate_strong_password(8, True, True))