# Write your solution here
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item) 

    return sorted(results)

if __name__ == "__main__":
    my_list = [3, 2, 1, 3, 2, 1, 3, 2, 1]
    print(distinct_numbers(my_list))