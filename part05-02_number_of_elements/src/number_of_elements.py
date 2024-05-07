# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    amt = []
    for part in my_matrix:
        add = part.count(element)
        amt.append(add)
    sm = sum(amt)

    return sm    
if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))