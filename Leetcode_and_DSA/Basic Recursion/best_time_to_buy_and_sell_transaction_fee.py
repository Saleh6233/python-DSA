"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

"""
from typing import List, Dict, Tuple


def maxProfit(self, prices: List[int], fee: int) -> int:
    n = len(prices)
    memo = {}

    def getMax(day: int, stock: int) -> int:

        if day == n:
            return 0

        if (day, stock) in memo:
            return memo[(day, stock)]

        if stock == 1:
            sell = (prices[day] - fee) + getMax(day + 1, 0)
            hold = 0 + getMax(day + 1, 1)
            profit = max(sell, hold)
            memo[(day, stock)] = profit
            return profit

        else:
            buy = -prices[day] + getMax(day + 1, 1)
            skip = 0 + getMax(day + 1, 0)
            profit = max(buy, skip)
            memo[(day, stock)] = profit
            return profit

    return getMax(0, 0)
