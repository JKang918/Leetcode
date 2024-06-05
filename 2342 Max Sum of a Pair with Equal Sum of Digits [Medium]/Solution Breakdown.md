## 2342. Max Sum of a Pair with Equal Sum of Digits

>Description: [2342. Max Sum of a Pair with Equal Sum of Digits](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/)\
You are given a **0-indexed** array `nums` consisting of **positive** integers. You can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the number `nums[i]` is equal to that of `nums[j]`.
Return *the **maximum** value of* `nums[i] + nums[j]` *that you can obtain over all possible indices `i` and `j` that satisfy the conditions.*


Constraints:

- <code>1 <= nums.length <= 10<sup>5</sup></code> 
- <code>1 <= nums[i] <= 10<sup>9</sup>/</code>


### Solution: 

```python
def maximumSum(nums: list[int]) -> int:
    ans = -1
    soddict = dict()
    # {sum of digits : max of all associated nums[i]s}
    for i in range(len(nums)):
        
        #sod being sum of digits
        sod = 0
        k = 0
        while nums[i]//(10**k) >= 10:
            sod += (nums[i]//(10**k)) % 10
            k += 1
        sod += (nums[i]//(10**k))

        if sod not in soddict:
            soddict[sod] = nums[i]
        else:
            ans = max(ans, soddict[sod] + nums[i])
            soddict[sod] = max(soddict[sod], nums[i])
    
    return ans
```

### Breakdown of Solution:

**Hash table**

Use the sum of digits as key and the associated `nums[i]` as values.

If there is no preexisting `nums[i]` then add it to the dictionary value and finish the loo.

If there is a preexisting dictionary value, update `ans = preexisting value + nums[i]`.\
And then, update dictionary value if `nums[i]` is greater than the preexisting value for future iterations.

While I used while loop to compute the sum of digits, but I found a clever way to get around this in here: [solution submitted by https://leetcode.com/u/akaghosting/](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/solutions/2292641/python-java-easy-solution/)

I modified the above to fit my variable names. Substitute below for line 23 to line 28 and it would work.

```python
#....   
        #sod being sum of digits
        sod = sum(int(digits) for digits in str(nums[i]))
#....
```

### Complexity Analysis:

Time Complexity: *O(n)*

- iteration of `nums` 

Space Complexity: *O(n)*

- storing constants and `soddict` and constants
