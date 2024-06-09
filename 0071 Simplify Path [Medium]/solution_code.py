def simplifyPath(path: str) -> str:
    path = path.split('/')
    
    stack = []

    #Forloop
    for char in path:

        #first slash
        if char == '' and not stack:
            stack.append(char)

        # Multiple consecutive slashes -> no push
        elif char == '':
            None

        # One lvl up is impossible
        elif char == '..' and stack[-1] == '':
            None

        # One lvl up
        elif char == '..' and stack[-1] != '':
            stack.pop()    
        
        # Current directory
        elif char == '.':
            None
            
        #normal case, including '...'
        else:
            stack.append(char)    

    #Forloop Ends

    
    # if the end result is '/'
    if stack == ['']: return '/'

    #otherwise, join them with '/' as the delimiter
    else:             return '/'.join(stack)
