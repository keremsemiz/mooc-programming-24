# Write your solution here
def sum_of_positives(my_list: list):
    newmylist = []
    for i in my_list:
        if i > 0:
            newmylist.append(i)
    
    return sum(newmylist)

    print("The result is", result)
if __name__ == "__main__":
    print(sum_of_positives([1, -1, 2, -2, 3, -3]))