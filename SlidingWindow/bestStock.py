#Python program to implement best time to buy and sell stock

def bestTime(prices):
    maxProfit = 0
    l,r = 0,1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1
    return maxProfit

print(bestTime([7,1,5,3,6,4]))