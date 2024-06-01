## 344. Reverse String 

>Description: [344. Reverse String](https://leetcode.com/problems/reverse-string/description/)\
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.


### Solution: 

```python
def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    left = 0
    right = len(s) - 1
    
    while left < right: 
        #swap the values
        s[left], s[right] = s[right], s[left]

        left  += 1
        right -= 1
```
### Breakdown of Solution:

**Two Pointers**

This problem is easily solved using two pointers.

Code above is quite intuitional; swap left character pointed by left with the right character pointed by right.\
One thing to take note of is the condition is "left < right". If this condition is not placed and both pointers iterate through the whole given string then s will not change. Because it is reversed twice.

### Complexity Analysis:

Time Complexity: *O(n)*

- *O(1n)* iterate s

Space Complexity: *O(1)*
    
