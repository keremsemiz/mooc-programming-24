# Write your solution here
def list_of_stars(list):
    for i in range(len(list)):
        print("*" * list[i])

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])