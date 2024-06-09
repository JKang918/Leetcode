def isValid(s: str) -> bool:
    
    paren = {'(' : ')', 
             '{' : '}', 
             '[' : ']'}
    
    stack = []

    for char in s:
        if char in paren:                    #opening parenthesis
            stack.append(char)
        else:                                #closing parenthesis
            if not stack:                    #in case it's an empty stack (exception)
                return False
            elif paren[stack.pop()] != char: #no matching
                return False
    
    if not stack: return True                #if all matched, at the end stack should be empty
    else: return False        