def line(length, text):
    if text == "" or text == " ":
        print("*" * length)
    else:
        print(text[0] * length)

def shape(length, letter, height, char):
    limit = (length - length) + 1
    for i in range(length):
        line(limit, letter)
        limit += 1
    for i in range(height):
        line(length, char)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")