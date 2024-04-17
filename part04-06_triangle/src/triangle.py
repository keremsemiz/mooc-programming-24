def line(length, text):
    if text == "" or text == " ":
        print("*" * length)
    else:
        print(text[0] * length)

def triangle(size):
    limit = (size - size) + 1
    for i in range(size):
        line(limit, "#")
        limit += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
