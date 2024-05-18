# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

        exedict[parts[0]] = sum(map(int, parts[1:8]))


for id, (first, last) in stddict.items():
    if id in exedict:
        exercises = exedict[id]
        print(f"{first} {last} {exercises}")
