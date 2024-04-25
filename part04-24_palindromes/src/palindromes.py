# Write your solution here
def palindromes(word):
    return word == word[::-1]:

def main():
     while True:
        word = input("Please type in a palindrome:")
        if palindromes(word):
            print(f"{word} is a palindrome!")
        else:
            print("that wasn't a palindrome")

if __name__ == "__main__":
    main()