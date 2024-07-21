## 3099. Harshad Number

>Description: [3099. Harshad Number](https://leetcode.com/problems/harshad-number/description/)\
Check out the link above for description and examples.

Constraints:

- `1 <= x <= 100`

### Solution 1 Converting to string: 

```python
def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    

    sod = sum(int(digit) for digit in list(str(x)))
    
    if x % sod == 0:
        return sod
    else:
        return -1
```


### Breakdown of Solution:

**Converting to a string**

Though the name is intriguing, Harshad Number itself is quite irrelvant in this problem. This problem is simply asking you to calculate sum of digits.

First, you can pefrom that by coverting data into string.

1. Covert given integer `x` into string
2. Parse the string
3. Convert each parsed character back into integer
4. Sum that all up

The code looks simple, but coverting data structures might not be desirable in many cases.

### Complexity Analysis:

Time Complexity: *O(n)*

- iterate the string (n being the number of digits)

Space Complexity: *O(n)* 

- lists

---

### Solution 2 while loop: 

```python
def sumOfTheDigitsOfHarshadNumber(x: int) -> int:
    
    #solution 1
    s = x
    sod = 0

    while s > 0:
        sod += s % 10
        s = s // 10

    if x % sod == 0:
        return sod
    else:
        return -1
```


### Breakdown of Solution:

**simple math calculation with while loop**

You can do the same task by simply implementing while loop.

### Complexity Analysis:

Time Complexity: *O(n)*

- while loop (n being the number of digits)

Space Complexity: *O(1)* 

- constants only

    
