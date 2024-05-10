# Write your solution here
def remove_smallest(numbers: list):
    m = min(numbers)
    numbers.remove(m)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)