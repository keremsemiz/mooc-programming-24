# Write your solution here
def add_student(students: dict, name: str):
    students[name] = ""
    return students

def add_course(students: dict, name: str, coursedata: tuple):
    if students[name] == "no completed courses" or students[name] == "": 
        students[name] = []
    
    students[name].append(tuple(coursedata))
    print(students)


def print_student(students: dict, name: str):
    if name not in students:    
        print(f"{name}: no such person in the database")
    else:
        print(f"{name}:")


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