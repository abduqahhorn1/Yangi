def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

input_prices = [7, 1, 5, 3, 6, 4]
output1 = max_profit(input_prices)
input_prices = [7, 6, 4, 3, 1]
output2 = max_profit(input_prices)
print(output1,output2) 