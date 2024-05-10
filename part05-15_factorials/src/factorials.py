# Write your solution here
def factorise(num: int):
    for i in range(1, num):
        num *= i
    return num

def factorials(n: int):
    newdict = {}
    for i in range(1, n + 1):
        newdict[i] = factorise(i)

    return newdict

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])