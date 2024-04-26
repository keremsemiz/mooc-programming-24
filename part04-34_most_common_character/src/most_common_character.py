# Write your solution here
def most_common_character(string):
    mcc = 0
    mccl = 0
    for char in string:
        if string.count(char) > mccl:
            mccl = string.count(char)
            mcc = char
    return mcc

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))