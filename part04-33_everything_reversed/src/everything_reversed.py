# Write your solution here
def everything_reversed(my_list: list):
    revlist = []
    for item in my_list:
        revlist.insert(0, item[::-1])
    return revlist

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)