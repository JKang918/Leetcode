def minimumCardPickup(cards: list[int]) -> int:
    
    ans = len(cards) + 1

    # {cardval : index}
    cardval = dict()
    for i in range(len(cards)):
        if cards[i] in cardval:
            ans = min(ans, i - cardval[cards[i]] + 1)
        cardval[cards[i]] = i
    
    if ans == len(cards) + 1: return -1
    else:                     return ans