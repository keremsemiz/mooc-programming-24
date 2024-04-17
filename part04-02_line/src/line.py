# Write your solution here
# You can test your function by calling it within the following block

def line(length, text):
    if text == "" or text == " ":
        print("*" * length)
    else:
        print(text[0] * length)


if __name__ == "__main__":
    line(5, "x")