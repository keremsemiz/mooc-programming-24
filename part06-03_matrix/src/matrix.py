# write your solution here
def totalsum(nums: list):
    tts = 0
    for num in nums:
        tts += num
    
    return tts

def totalmax(nums: list):
    ttm = -10000000000
    for num in nums:
        if num > ttm:
            ttm = num
    
    return ttm

def matrix_sum():
    with open("matrix.txt") as matrixfile:
        ttsum = 0
        for line in matrixfile:
            line = line.replace("\n", "")
            parts = line.split(",")
            nums = []
            for num in parts:
                nums.append(int(num))
            ttsum += totalsum(nums)

    return ttsum

def matrix_max():   
    with open("matrix.txt") as matrixfile:
        ttmax = -10000000000
        for line in matrixfile:
            line = line.replace("\n", "")
            parts = line.split(",")
            nums  = []
            for num in parts:
                nums.append(int(num))
            if ttmax < totalmax(nums):
                ttmax = totalmax(nums)

    return ttmax

def row_sums():
    with open("matrix.txt") as matrixfile:
        ttsums = []
        for line in matrixfile:
            line = line.replace("\n", "")
            parts = line.split(",")
            nums = []
            for num in parts:
                nums.append(int(num))
            ttsums.append(totalsum(nums))

    return ttsums


if __name__ =="__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())