# Write your solution here
def length_of_longest(my_list: list):
    for strings in my_list:
        length = len(my_list[0])
        for i in my_list:
            if len(i) > length:
                length = len(i)
    return length

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)