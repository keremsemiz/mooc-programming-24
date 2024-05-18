# write your solution here
def largest():
    with open("numbers.txt") as file:
        numbers = []
        for num in file:
            numbers.append(int(num))

    if len(numbers) > 0:
        numbers[0] = max(numbers)
    print(numbers[0])

if __name__ == "__main__":
    largest()