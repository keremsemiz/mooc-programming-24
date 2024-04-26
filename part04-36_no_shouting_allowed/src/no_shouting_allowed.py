# Write your solution here
def no_shouting(my_list: list):
    newlist = []
    for item in my_list:
        if item.isupper() != True:
            newlist.append(item)
    return newlist
    
if __name__ == "__main__":    
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)