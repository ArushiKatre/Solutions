def maxProfit(prices):
    min_price = prices[0]
    maxdiff = 0

    for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > maxdiff:
                maxdiff = profit

    return maxdiff

