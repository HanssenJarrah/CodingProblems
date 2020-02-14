"""
Given a list showing the stock price for a company each time unit, find the profit that would have been made if
buying and selling at the best possible time.
"""

stock_prices = [7, 1, 5, 3, 6, 4]


def max_profit(prices):
    if len(prices) < 2:
        return 0

    best_buy = prices[0]
    best_sell = prices[1]
    for buy_i in range(len(prices) - 1):
        for sell_i in range(buy_i, len(prices)):
            if prices[sell_i] - prices[buy_i] > best_sell - best_buy:
                best_buy = prices[buy_i]
                best_sell = prices[sell_i]
    profit = best_sell - best_buy
    if profit > 0:
        return profit
    return 0


def main():
    profit = max_profit(stock_prices)
    print(profit)


if __name__ == "__main__":
    main()