def get_num_words (text):
    words = text.split()
    return len(words)

def count_characters (text: str):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters
    

