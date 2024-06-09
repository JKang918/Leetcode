def removeDuplicates(s: str) -> str:
    
    if len(s) == 1: return s
    
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return "".join(stack)