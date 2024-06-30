## 0009. Palindrome Number

>Description: [0009. Palindrome Number](https://leetcode.com/problems/palindrome-number/description/)\
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

Constraints:

- <code>-2<sup>31</sup> - 1 <= x <= 2<sup>31</sup> - 1</code> 

### Solution 1  string: 

```python
def isPalindrome(x: int) -> bool:
    
    x = str(x)  #turn int x into string
    x = list(x) #parse string x
    
    #two pointers
    left = 0
    right = len(x) - 1

    while left < right and left < len(x) and right >= 0:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    
    return True
    
```
### Breakdown of Solution:

**Two Pointers**

1. Convert input integer `x` into string
2. Parse it into a list of strings
3. Using two pointers, check whether the list of strings are palindrome

### Complexity Analysis:

Time Complexity: *O(n)*

- check the list with length of n

Space Complexity: *O(1)*



### Solution 2  Using decimals: 

```python
def isPalindrome(x: int) -> bool:
    if x < 0: 
        return False

    xtemp  = x                          #to make the original input x intact
    xreversed = 0
    while xtemp != 0:
        if xreversed != 0:
            xreversed *= 10             #push to the right
        xreversed += xtemp % 10         #store in xpalin the last digit of x
        xtemp = xtemp // 10             #discard the last digit of x (push to the left)
    
    return x == xreversed
```
### Breakdown of Solution:

This method is specific to this problem.

Before beginning, rule out the negative number cases.

After that, declare another variable, `xreversed` to store the reversed number of `x`.

The idea is simple.

1. Store the remnant of x
2. .. times 10 in the next iteration.

With this, if `x` is equal to `xreversed`, it is a palindrome number.


### Complexity Analysis:

Time Complexity: *O(n)*

- while loop

Space Complexity: *O(1)*

- only constants are stored.
