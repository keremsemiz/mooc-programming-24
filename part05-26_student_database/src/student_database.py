# Write your solution here
def add_student(database: dict, student: str):
    database[student] = ""
    return database

def add_course(database: dict, student: str, course: tuple):
    test = []
    final = []

    if database[student] == "no completed courses" or database[student] == "": 
        database[student] = []

    database[student].append(tuple(course))
    copy = sorted(database[student])[::-1]

    for key, value in database.items():
        if value == "":
            continue
    
    for subject, grade in copy:
        if subject not in test and grade > 0:
            test.append(subject)
            test.append(grade)

    for i in range(len(test)):
        pair = test[i], test[i + 1]
        if pair not in final and i % 2 == 0:
            final.append(pair)

    database[student] = final

    return database


def print_student(database: dict, student: str):
    defaultoutput = "no completed courses"

    if student in database:
        print(f"{student}: ")

        if database[student] == "":
            database[student] = defaultoutput
            print(f" {database[student]}")


        else:
            if len(database[student]) > 0:
                avg = 0
                print(f" {len(database[student])} completed courses:")

                for key, value in database[student]:
                    print(f"  {key} {value}")
                    average += value

                if average > 0:
                    average = average / len(database[student])
                    print(" average grade", average)
            else:
                print(" "+ defaultoutput)

    else:
        print(f"{student}: no such person in the database")

    return database


def summary(database: dict):
    totalstudents = 0
    mostcoursescompleted = 0
    mostcoursesname = ""
    bestaverage = 0
    bestaveragename = ""
    bestaveragecopy = 0
    bestaveragenamecopy = ""

    for key, value in database.items():
        totalstudents += 1
        if mostcoursescompleted > len(value):
            mostcoursescompleted = len(value)
            mostcoursesname = key


        for a, b in value:
            bestaveragecopy += b
            bestaveragenamecopy = key
        bestaveragecopy = bestaveragecopy / len(value)


        if bestaverage < bestaveragecopy:
            bestaverage = bestaveragecopy
            bestaveragename = bestaveragenamecopy
    
        bestaveragecopy = 0

    print("students", totalstudents)
    print("most courses completed", mostcoursescompleted, mostcoursesname)
    print("best average grade", bestaverage, bestaveragename)

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Introduction to Programming", 2))

    add_course(students, "Peter", ("Data Structures and Algorithms", 0))

    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    summary(students)