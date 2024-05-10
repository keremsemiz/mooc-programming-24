# Write your solution here
def histogram(string: str):
    amount = {}
    for i in string:
        if i not in amount:
            amount[i] = 0
        amount[i] += 1

    for key, value in amount.items():
        print(f"{key} {value* "*"}")



if __name__ == "__main__":
    histogram("statistically")