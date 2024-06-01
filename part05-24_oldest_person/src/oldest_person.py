def oldest_person(people: list) -> str:
    oldest_name = people[0][0]
    oldest_year = people[0][1]
    
    for person in people[1:]:
        name, birth_year = person
        if birth_year < oldest_year:
            oldest_name = name
            oldest_year = birth_year
    
    return oldest_name

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
