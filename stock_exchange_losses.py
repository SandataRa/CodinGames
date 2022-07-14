import sys
 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
 
n = int(input())
prices = [int(s) for s in input().split()]
lowest = int(prices.index(min(prices)))+1
losses = [] # history of losses
 
if (lowest == 0) and (int(prices.index(max(prices)))+1 == len(prices)):
    print(0)
else:
    highest = int(prices.index(max(prices)))
    if highest < lowest:
        gap = min(prices) - max(prices)
        print(gap)
    else:
        while(len(prices) > 1):
 
            lowest = int(prices.index(min(prices)))+1
            sub_prices = prices[0:lowest]
            peak_price = max(sub_prices)
 
            p = min(prices) - max(sub_prices) # maximum loss
            losses.append(p)
            prices = prices[lowest:]
 
print(min(losses))