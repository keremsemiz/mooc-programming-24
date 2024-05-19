# wwite your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")

stddict = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.strip().split(';')
        if parts[0] == 'id':
            continue
        stddict[parts[0]] = (parts[1], parts[2])


exedict = {}

with open(exercise_data) as newer_file:
    for line in newer_file:
        parts = line.strip().split(';')
        if parts[0] == 'id':
            continue

        exedict[parts[0]] = sum(map(int, parts[1:]))

exadict = {}

with open(exam_data) as newer_file:
    for line in newer_file:
        parts = line.strip().split(';')
        if parts[0] == 'id':
            continue

        exadict[parts[0]] = sum(map(int, parts[1:]))

def points_to_grade(points):
    if points <= 14:
        return 0
    elif points <= 17:
        return 1
    elif points <= 20:
        return 2
    elif points <= 23:
        return 3
    elif points <= 27:
        return 4
    else:
        return 5


for id, (first, last) in stddict.items():
    if id in exedict and id in exadict:
        exercise_points = (exedict[id] // 4)
        total_points = exercise_points + exadict[id]
        grade = points_to_grade(total_points)
        print(f'{first} {last} {grade}')

    else:
        print(f'{first} {last} 0')
