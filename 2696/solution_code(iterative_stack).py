def minLength(s: str) -> int:
    stack = []
    charmatch = {
        'A': 'B',
        'C': 'D'
    }

    for char in s:
        if stack and char == charmatch.get(stack[-1], 0):
            stack.pop()
        else:
            stack.append(char)
    
    return len(stack)