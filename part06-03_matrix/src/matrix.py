# write your solution here
def totalsum(nums: list):
    tt = 0
    for num in nums:
        tt += num
    
    return tt

def totalmax(nums: list):


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
        ttmax = 0
        for line in matrixfile:
            line = line.replace("\n", "")
            parts = line.split(",")
            nums  = []
            for num in parts:
                nums.append(int(num))

    return ttmax

def row_sums():
    rwsums = []
    with open("matrix.txt") as matrixfile:
        for line in matrixfile:
            line = line.replace("\n", "")
            parts = line.split(",")
            nums = []
            for num in parts:
                nums.append(int(num))
                rwsums.append(sum(nums))


if __name__ =="__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())