# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    frc = []
    for i in range(amount):
        frc.append(Fraction(1, amount))

    return frc

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))