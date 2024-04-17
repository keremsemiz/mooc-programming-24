# Write your solution here
def spruce(size):
    print("a spruce!")
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)
    print(" " * (size - 1) + "*" + " " * (size) )




# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)