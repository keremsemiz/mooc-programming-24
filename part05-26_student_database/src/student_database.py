# Write your solution here
def add_student(students: dict, name: str):
    students[name] = ""
    return students

def add_course(students: dict, name: str, coursedata: tuple):
    test = []
    list_tuple = []

    if students[name] == "no completed courses" or students[name] == "": 
        students[name] = []
    
    students[name].append(tuple(coursedata))
    #print(students)

    copy = sorted(students[name])[::-1]
    #print(copy)

    for key, value in students.items():
        if value == "": #no value then skip
            continue

    for subject, grade in copy:
        if subject not in test and grade > 0:
            test.append(subject)
            test.append(grade)


    for i in range(len(test)):
        pair = test[i], test[i + 1]
        if pair not in list_tuple and i % 2 == 0:
            list_tuple.append(pair)


    students[name] = list_tuple

    return students




def print_student(students: dict, name: str):
    default = "no completed courses"
    
    if name not in students:    
        print(f"{name}: no such person in the database")
    
    else:
        print(f"{name}")
        print(f" {len(students[name])} completed courses:")




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