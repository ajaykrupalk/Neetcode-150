#Python program to implement Min Cost Climbing Stairs

def minCost(cost):
    cost.append(0)

    for i in range(len(cost)-3, -1, -1):
        cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        
    return min(cost[0], cost[1])