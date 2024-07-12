## 0125. Valid Palindrome

>Description: [0125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150)\
check the link above

Constraints:

- <code>1 <= s.length <= 2*10<sup>5</sup></code> 
- `s` consists only of printable ASCII characters (alphabets and digits).


### Solution: 

```python
def isPalindrome(s: str) -> bool:
    n = len(s)
    left = 0
    right = n - 1

    while left < right:
        
        #to skip non-alphabet, non-number characters
        while left < right and not s[left].isalnum():
            left += 1
        
        #to skip non-alphabet, non-number characters
        while left < right and not s[right].isalnum():
            right -= 1

        #do not distinguish upper and lower cases
        if s[left].lower() != s[right].lower():
            #if not palindrome
            return False


        left += 1
        right -= 1
    #while loop ends if palindrome
    return True       
```
### Breakdown of Solution:

**Two Pointers**

- `left` sweeps from the left of the string, `right` do the same from the right end.
- In this problem we ignore all the non-alphabet, non-number characters. Inner while statements are there for that.
- Also, in accordance with the problem description, upper letters and lower letters are not distinguished. So we treat them as if they are all lower letters in this case. Of course, `.upper()` can be used as well instead.
- When the left section of the string is equal to the right section of the string, the outer while loop ends and return `True`.

### Complexity Analysis:

Time Complexity: *O(n)*

- linearly correlated with the length of the string

Space Complexity: *O(1)*

- only constants
