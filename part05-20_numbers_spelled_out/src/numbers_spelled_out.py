# Write your solution here
def dict_of_numbers():
    numbersspelled = {}
    numbers = []
    for i in range(100):
        numbers.append(i)

    wor0 = ['zero']
    t10 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    t20 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    t100 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    rem = []

    for i in range(len(t100)):
        rem.append(t100[i])
        for j in range(len(t10)):
            rem.append(t100[i] + "-" + t10[j])


    final = []
    final.append(wor0[0])

    for i in t10:
        final.append(i)
    
    for i in t20:
        final.append(i)

    for i in rem:
        final.append(i)
    
    numbersspelled = {numbers[i] : final[i] for i in range(100)}

    return numbersspelled
if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])