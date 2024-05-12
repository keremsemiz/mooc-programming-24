# Write your solution here
def create_tuple(x: int, y: int, z: int):
    lst = []
    lst.append(x)
    lst.append(y)
    lst.append(z)
    lst.sort()
    min = lst[0]
    max = lst[2]

    sm = x + y + z

    tpl = (min, max, sm)

    return tpl

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))