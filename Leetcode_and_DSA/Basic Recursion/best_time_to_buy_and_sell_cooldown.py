"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}

        def getMax(day: int, stock: int) -> int:

            if day >= n:
                return 0

            if (day, stock) in memo:
                return memo[(day, stock)]

            if stock == 1:
                sell = prices[day] + getMax(day + 2, 0)
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
