# Write your solution here
def pointscalculator(inpt):
    space = inpt.find(" ")
    exampoints = int(inpt[:space])
    exercisepoints = int(inpt[space+1:])

    exercisepercent = exercisepoints // 10
    totalpoints = exampoints + exercisepercent

    return totalpoints, exampoints


def grade(totalpoints):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if totalpoints >= boundary[i]:
            return i

def mean(totalpoints):
    return sum(totalpoints) / len(totalpoints)


def main():
    points = []
    grades = [0] * 6
    while True:
        inpt = input("Exam points and exercises completed: ")
        if inpt == "":
            break
        
        totalpoints, exampoints = pointscalculator(inpt)
        points.append(totalpoints)
        grd = grade(totalpoints)
        if exampoints < 10:
            grd = 0
        grades[grd] += 1
    
    passpercent = 100 * (len(points) - grades[0]) / len(points)

    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {passpercent:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")


main()