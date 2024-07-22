from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    
    strIndex = 0
    charIndex = 0
    word2len = len(word2) #strIndex
    word2charlen = [len(string) for string in word2] #charIndex #this part is critical
    
    #traverse following each character in word1 
    for string in word1:
        for char in string:
            #either word2 is exhausted too early or not mathcing
            if strIndex == word2len or (char != word2[strIndex][charIndex]):
                return False
            
            charIndex += 1

            if charIndex == word2charlen[strIndex]:
                strIndex += 1
                charIndex = 0

    #word2 exhaustion check
    if charIndex != 0 or strIndex != word2len:
        return False
    
    return True