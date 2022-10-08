#Python program to implement Cheapest Flights within K Stops

def findCheapest(n, flights,src,dst,k):
    prices = [float("inf")]*n
    prices[src] = 0

    for i in range(k+1):
        tmpPrices = prices.copy()
        for s,d,p in flights:
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tmpPrices[d]:
                tmpPrices[d] = prices[s] + p
        prices = tmpPrices

    return -1 if prices[dst] == float("inf") else prices[dst]