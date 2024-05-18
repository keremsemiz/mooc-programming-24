# write your solution here
studentinp = input("Student information: ")
stddict = {}

with open(studentinp) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        stddict[parts[0]] = (parts[1], parts[2])

exerciseinp = input("Exercises completed: ")
exedict = {}

with open(exerciseinp) as newer_file:
    for line in newer_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        exedict[parts[0]] = sum(map(int, parts[1:7]))

    
    for id, name in stddict.items():
        exercises_total = sum(exedict[id])
        print(f'{name[0]} {name[1]} {exercises_total}')