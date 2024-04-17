def line(length, text):
    if text == "" or text == " ":
        print("*" * length)
    else:
        print(text[0] * length)

def square(size, character):
    for i in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")