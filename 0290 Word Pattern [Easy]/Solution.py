def wordPattern(pattern: str, s: str) -> bool:
    s = str.split(s)
    patt_to_word = dict()
    word_to_patt = dict()
    
    if len(pattern) != len(s):
        return False
    
    for char, word in zip(pattern, s):
        
        if char in patt_to_word:
            if patt_to_word[char] != word:
                return False
        
        if word in word_to_patt:
            if word_to_patt[word] != char:
                return False

        #first one-to-one match
        patt_to_word[char] = word
        word_to_patt[word] = char
    
    return True