# Write your solution here
def list_sum(a: list, b: list):
    newsum = []
    for i in range(len(a)):
        newsum.append(a[i] + b[i])
    return newsum

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))