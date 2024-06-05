## 2260. Minimum Consecutive Cards to Pick Up

>Description: [2260. Minimum Consecutive Cards to Pick Up](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/)\
You are given an integer array `cards` where `cards[i]` represents the **value** of the `ith` card. A pair of cards are **matching** if the cards have the **same** value.\
Return *the **minimum** number of **consecutive** cards you have to pick up to have a pair of **matching** cards among the picked cards.* If it is impossible to have matching cards, return -1.

Constraints:

- <code>1 <= cards.length <= 10<sup>5</sup></code> 
- <code>0 <= cards[i] <= 10<sup>6</sup>/</code> 

### Solution: 

```python
def minimumCardPickup(cards: list[int]) -> int:
    
    #ans can never go over len(cards)
    ans = len(cards) + 1

    # {cardval : index}
    cardval = dict()
    for i in range(len(cards)):
        if cards[i] in cardval:                         #if a certain number on card already appeared before
            ans = min(ans, i - cardval[cards[i]] + 1)   #consecutive cards to pick up is i (index of current card) + 1 - card[cards[i]] (index of previous card with the same number)
        cardval[cards[i]] = i                           #update index information with the most recent one
    
    
    if ans == len(cards) + 1: return -1 #ans can never go over len(cards). So if it's len(cards) + 1, it means ans never got updated with valid information. 
    else:                     return ans
```
### Breakdown of Solution:

**Hash table**

Use the number on cards as key and their most recent indices as values.

Consecutive cards to pick up can be easily computed using index information.

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of `cards`

Space Complexity: *O(n)*

- storing constants and `cardval`
