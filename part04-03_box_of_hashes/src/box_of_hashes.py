def line(length, text):
    if text == "" or text == " ":
        print("*" * length)
    else:
        print(text[0] * length)

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
