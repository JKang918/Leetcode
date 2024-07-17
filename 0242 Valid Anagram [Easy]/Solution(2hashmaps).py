def isAnagram(s: str, t: str) -> bool:
 
    hash1 = dict()
    hash2 = dict()

    for char in s:
        if char not in hash1:
            hash1[char] = 1
        else:
            hash1[char] += 1
    
    for char in t:
        if char not in hash2:
            hash2[char] = 1
        else:
            hash2[char] += 1
    
    return hash1 == hash2