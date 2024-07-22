from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    
    list1 = []
    list2 = []

    for char in word1:
        list1.extend(char)
    
    for char in word2:
        list2.extend(char)
    
    return list1 == list2