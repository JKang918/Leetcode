def lengthOfLastWord(s: str) -> int:
    
    i = -1
    length = 0
    
    #remove all the spaces in the last part until the last word shows up
    while (-i) <= len(s) and s[i] == " ":
        i -= 1
    
    #Then count the letters in last word
    while (-i) <= len(s) and s[i] != " ":
        i -= 1
        length += 1
    
    return length