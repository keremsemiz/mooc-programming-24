# write your solution here
def read_fruits():
    frtdict = {}
    with open("fruits.csv") as csvfile:
        for line in csvfile:
            line = line.replace("\n", "")
            parts = line.split(";")
            frtdict[parts[0]] = float(parts[1]) 
    
    return frtdict

if __name__ == "__main__":
    print(read_fruits())