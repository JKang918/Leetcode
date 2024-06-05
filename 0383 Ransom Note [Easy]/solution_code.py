def canConstruct(ransomNote: str, magazine: str) -> bool:
    
    #improve speed
    if len(ransomNote) > len(magazine): return False

    charcount = dict()

    for char in magazine:
        charcount[char] = charcount.get(char, 0) + 1
    
    for char in ransomNote:
        if charcount.get(char, 0) == 0: return False
        else:
            charcount[char] -= 1
    
    return True