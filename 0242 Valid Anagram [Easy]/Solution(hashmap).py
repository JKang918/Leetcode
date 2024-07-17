def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    cnt = dict()
    
    for schar, tchar in zip(s, t):
        if schar not in cnt:
            cnt[schar] = 1
        elif schar in cnt:
            cnt[schar] += 1
        
        if tchar not in cnt:
            cnt[tchar] = -1
        elif tchar in cnt:
            cnt[tchar] -= 1
    
    for counts in cnt.values():
        if counts != 0:
            return False
    return True