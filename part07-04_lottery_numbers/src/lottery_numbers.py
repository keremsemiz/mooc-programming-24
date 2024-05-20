# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):
    nums = []
    while len(nums) < a
        pick = randint(lower, upper)
        if pick not in nums:
            nums.append(pick)
        else:
            continue

    return sorted(nums)


if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)