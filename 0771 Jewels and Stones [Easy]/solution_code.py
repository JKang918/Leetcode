def numJewelsInStones(jewels: str, stones: str) -> int:

    jew = set(jewels)

    ans = 0
    for s in stones:
        if s in jew: ans += 1
    
    return ans