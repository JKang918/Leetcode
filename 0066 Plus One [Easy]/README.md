## 66. Plus One

>Description: [66. Plus One](https://leetcode.com/problems/plus-one/)\
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.\
Increment the large integer by one and return the resulting array of digits.

Constraints:

- <code>1 <= digits.length <= 100</code>
- <code>0 <= digits[i] <= 9</code>
- `digits` does not contain any leading `0`'s.


### Solution: 

```python
def plusOne(self, digits: list[int]) -> list[int]:
    #iterate from the back
    n = len(digits)
    for i in range(n):
        idx = n - 1 - i

        if digits[idx] == 9:
            digits[idx] = 0
        
        else:
            digits[idx] += 1
            return digits
    
    return [1] + digits
```

### Breakdown of Solution:

**Iteration from the back**

Let's begin with the `else` statement:

When the last number is not `9`, just +1. Then return `digits`.

However, When the last number is `9`, then make it `0` and iterate to the next number. If it's not `9`, again, go to the `else` statement and return `digits`.

What happens if the digits is all `9`s? For example, `9999`?

In this case, digits will be exhausted, for loop ends without returning digits (=without running the if statement) and at the end digitis will be `0000`.

But we need to return `10000` instead of `0000`.

So at the end, '[1]' need to be appended... from the front! This is done with `[1] + digits`.

### Complexity Analysis:

Time Complexity: *O(n)*

- iterate `digits`

Space Complexity: *O(1)*

- only constants