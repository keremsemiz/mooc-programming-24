# Write your solution here
def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    word = ""
    for char in string:
        if char in vowels:
            char = ""
        word += char
    
    return word

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))