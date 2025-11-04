#eserczio funzione trova

def search(word, character, start_position):
    index = start_position
    while index < len(word):
        if word[start_position] == character:
            return index
        index = index +1
    return -1