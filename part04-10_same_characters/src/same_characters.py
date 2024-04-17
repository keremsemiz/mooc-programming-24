# Write your solution here
def same_chars(word, in1, in2):
    if in1 >= len(word) or in2 >= len(word):
        return False
    if word[in1] == word[in2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 6, 7))