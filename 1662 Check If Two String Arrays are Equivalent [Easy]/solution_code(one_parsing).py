from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    list2 = []
    
    for string in word2:
        list2.extend(string)
    
    word2len = len(list2)
    
    index = 0
    for string in word1:
        for char in string:
            if index == word2len or list2[index] != char:
                return False
            index += 1
    
    if index == word2len:
        return True
    return False