def maxProfit(prices):
    #最低价格
    minprice = float('inf')
    #最大利润
    maxprofit = 0

    for item in prices:
        minprice = min(minprice,item)
        if item - minprice > maxprofit:
            maxprofit = item - minprice
    return maxprofit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))