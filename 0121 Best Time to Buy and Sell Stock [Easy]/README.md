## 0121. Best Time to Buy and Sell Stock

>Description: [0121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150)\
Check out the link above for description.

Constraints:

- <code>1 <= price.length <= 10<sup>5</sup></code> 
- <code>0 <= prices[i] <= 10<sup>4</sup></code> 

### Solution 1  Burte Force: 

```python
def maxProfit(prices: list[int]) -> int:

    #brute force #two pointers
    n = len(prices)
    profit = 0
    for t in range(n - 1):
        for t1 in range(t+1, n):
            #check all pairs
            #if profit greater than previous max, update
            if prices[t1] - prices[t] > profit:
                profit = prices[t1] - prices[t]

    return profit
```
### Breakdown of Solution:

**checking all pairs**

One intuitive approach would be checking all possible pairs.

Using a nested for loop, generate all possible pairs and calculate `profit` every time.

`t1` starts from `t + 1`: stock sales only can happen after purchase.


### Complexity Analysis:

Time Complexity: *O(n<sup>2</sup>)*

- nested for loop

Space Complexity: *O(1)*



### Solution 2  One iteration: 

```python
def maxProfit(prices: list[int]) -> int:

    profit = 0
    purchase = prices[0]

    #time series
    for t in range(1, len(prices)):
        #t+1 price is smaller than t price -> assume purchase at t+1
        if purchase > prices[t]:
            purchase = prices[t]
        
        #t+1 price is larger than t price -> assume selling at t+1. If the profit is greater than previous max, update.
        if purchase < prices[t]:
            profit = max(prices[t] - purchase, profit)
        
        #t+1 price = t price -> no need to do anything

    return profit
```
### Breakdown of Solution:

**One iteration**

Without checking all pairs, just one iteration is suffice to solve this problem.

Whenever price level lower than previous `purchase` comes up: update `purchase` to that price and assume purchasing stock that day.

Whenever price level higher, assuming selling the stock that day and compute `profit` if sales occurr: if it is higher than previous `profit`, update `profit`.

### Complexity Analysis:

Time Complexity: *O(n)*

- one for loop

Space Complexity: *O(1)*
