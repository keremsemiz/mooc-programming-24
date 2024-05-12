# Write your solution here
def oldest_person(people: list):
    for i in people:
        oldest = max(people[i][1])

    return oldest[0]

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    p5 = ('Emily', 2014)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))