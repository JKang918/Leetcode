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