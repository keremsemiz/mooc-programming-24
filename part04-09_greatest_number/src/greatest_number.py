# Write your solution here
def greatest_number(a, b, c):
    numbers = []
    numbers.append(a)
    numbers.append(b)
    numbers.append(c)
    numbers.sort()
    return numbers[2]
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(8, 2, 1)
    print(greatest)