"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold than one share of the stock.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

"""

from typing import List, Dict, Tuple


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return maximum profit using recursion + memoization.

        Time complexity: O(n) where n = len(prices). There are at most 2*n unique states
        (day, stock), and each state is computed once.

        Space complexity: O(n) due to the memoization dictionary (O(2*n) entries)
        and the recursion call stack (depth up to n).
        """
        n = len(prices)
        memo: Dict[Tuple[int, int], int] = {}

        def getMax(day: int, stock: int) -> int:
            # Base case: no more days
            if day == n:
                return 0

            # Return cached result if available
            if (day, stock) in memo:
                return memo[(day, stock)]

            if stock == 1:
                # Option 1: sell today -> gain prices[day], move to next day without stock
                sell = prices[day] + getMax(day + 1, 0)
                # Option 2: hold the stock through today
                hold = getMax(day + 1, 1)
                profit = max(sell, hold)
            else:
                # stock == 0
                # Option 1: buy today -> pay prices[day], move to hold state
                buy = -prices[day] + getMax(day + 1, 1)
                # Option 2: skip buying today
                skip = getMax(day + 1, 0)
                profit = max(buy, skip)

            # Cache and return
            memo[(day, stock)] = profit
            return profit

        return getMax(0, 0)


if __name__ == "__main__":
    # Example testcases from the prompt
    examples = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
    ]

    solver = Solution()
    for prices, expected in examples:
        res = solver.maxProfit(prices)
        print(f"prices={prices} -> max profit = {res} (expected: {expected})")
