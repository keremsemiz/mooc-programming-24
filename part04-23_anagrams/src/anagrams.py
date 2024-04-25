# Write your solution here
def anagrams(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

if __name__ == "__main__":
    anagrams("john", "hans")