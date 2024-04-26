# Write your solution here
def all_the_longest(my_list: list):
    longest = 0
    newlist = []

    for i in my_list:
        if len(i) >= longest:
            longest = len(i)
        
    for i in my_list:
        if len(i) == longest:
            newlist.append(i)

    return newlist

if __name__ == "__main__":
    my_list = ['Alan', 'Steve', 'Seymour']
    result = all_the_longest(my_list)
    print(result)