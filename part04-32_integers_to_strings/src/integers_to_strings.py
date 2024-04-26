# Write your solution here
def formatted(my_list: list):
    newlist = []
    for i in my_list:
        num = "{:.2f}".format(i)
        newlist.append(num)
    return newlist

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)
