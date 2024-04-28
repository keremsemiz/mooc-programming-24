# Write your solution here
def longest(strings: list):
    longest = strings[0]
    for word in strings:
        if len(word) > lenlongest:
            longest = word
    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))