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