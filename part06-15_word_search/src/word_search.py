def read_words(filename: str) -> list:
    words = []
    with open(filename) as file:
        for word in file:
            words.append(word.strip())
    return words

def no_wildcard(words: list, search_term: str):
    finalwords = []
    for word in words:
        if word == search_term:
            finalwords.append(word)
    return finalwords

def dot_wildcard(words: list, search_term: str):
    finalwords = []
    for word in words:
        if len(word) == len(search_term):
            same = True
            for wcharacter, scharacter in zip(word, search_term):
                if scharacter != '.' and wcharacter != scharacter:
                    same = False
                    break
            if same:
                finalwords.append(word)
    return finalwords

def asterisk_wildcard(words: list, search_term: str):
    finalwords = []
    if search_term.startswith('*'):
        search_term = search_term[1:]
        for word in words:
            if word.endswith(search_term):
                finalwords.append(word)
    elif search_term.endswith('*'):
        search_term = search_term[:-1]
        for word in words:
            if word.startswith(search_term):
                finalwords.append(word)
    return finalwords

def find_words(search_term: str):
    words = read_words("words.txt")

    if '*' not in search_term and '.' not in search_term:
        return no_wildcard(words, search_term)
    elif '*' in search_term:
        return asterisk_wildcard(words, search_term)
    elif '.' in search_term:
        return dot_wildcard(words, search_term)