"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

"""
from __future__ import annotations
from typing import Dict


class Solution:
    memo: Dict[int, int] = {0: 0, 1: 1}

    def fib(self, n: int) -> int:

        assert n >= 0 and int(n) == n, "Non negative integer error!"
        if n in self.memo:
            return self.memo[n]
        else:

            res = self.fib(n-1) + self.fib(n-2)
            self.memo[n] = res
            return res


def iterative_fib(n: int) -> int:
    """
    Compute fib(n) iteratively in O(n) time and O(1) extra space.

    This is used as a safe fallback when recursion depth might be exceeded.
    """
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def prompt_for_n(default: int = 10) -> int:
    """
    Prompt the user to enter a non-negative integer. If the user presses Enter,
    return the provided default.
    """
    raw = input(
        f"Enter a non-negative integer n (press Enter for default {default}): ").strip()
    if raw == "":
        return default
    try:
        n = int(raw)
    except ValueError:
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be non-negative.")
    return n


def main() -> None:
    try:
        n = prompt_for_n()
    except ValueError as exc:
        print(f"Input error: {exc}")
        return

    solver = Solution()

    try:
        # Try the memoized recursive approach first
        result = solver.fib(n)
    except RecursionError:
        # If recursion limit is hit, fall back to iterative algorithm
        print("RecursionError: recursion depth exceeded. Falling back to iterative method.")
        result = iterative_fib(n)

    print(f"fib({n}) = {result}")


if __name__ == "__main__":
    main()
