"""
Given a list showing the stock price for a company each time unit, find the profit that would have been made if
buying and selling at the best possible time.
"""

stock_prices = [7, 1, 5, 3, 6, 4]


def max_stock_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


def main():
    profit = max_stock_profit(stock_prices)
    print(profit)


if __name__ == "__main__":
    main()