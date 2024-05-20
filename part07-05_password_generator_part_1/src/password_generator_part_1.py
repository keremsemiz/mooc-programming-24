# Write your solution here
from random import randint, choice
from string import ascii_letters

def generate_password(length: int):
    output = ''
    while len(output) < length:
        output += choice(ascii_letters.lower())

    return output

if __name__ == "__main__":
    print(generate_password(25))