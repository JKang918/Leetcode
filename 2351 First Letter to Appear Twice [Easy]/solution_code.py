def repeatedCharacter(s: str) -> str:
    seen = set()
    for char in s:
        if char not in seen: seen.add(char)
        else: return char