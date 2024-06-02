# Write your solution here
def readFile(filename: str) -> list:
    content = []
    with open(filename) as newFile:
        for line in newFile:
            line = line.strip()
            parts = line.split(';')
            content.append(parts)
    return content

def evaluate_data(content: list, correct_file_name: str, incorrect_file_name: str):
    open(correct_file_name, 'w').close()
    open(incorrect_file_name, 'w').close()
    correctfile = open(correct_file_name, 'w')
    incorrectfile = open(incorrect_file_name, 'w')
    
    for solution in content:
        if eval(solution[1]) == int(solution[2]):
            correctfile.write(';'.join(solution) + '\n')
        else:
            incorrectfile.write(';'.join(solution) + '\n')
    
    correctfile.close()
    incorrectfile.close()

def filter_solutions():
    content = readFile("solutions.csv")
    evaluate_data(content, 'correct.csv', 'incorrect.csv')