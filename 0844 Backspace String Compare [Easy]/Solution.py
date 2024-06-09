def buildingStack(s: str) -> str: #make it a function because the same process is repeated for s and t
    stack = []
    for c in s:
        if c != "#":
            stack.append(c)
        if c == "#" and stack:
            stack.pop()
    return "".join(stack)


def backspaceCompare(s: str, t: str) -> bool:
    
    return buildingStack(s) == buildingStack(t) 