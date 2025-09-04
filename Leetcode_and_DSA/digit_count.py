"""
Given a number n, the task is to return the count of digits in this number.

Example:

Input: n = 1567
Output: 4
Explanation: There are 4 digits in 1567, which are 1, 5, 6 and 7.

Input: n = 255
Output: 3
Explanation: There are 3 digits in 256, which are 2, 5 and 5.

"""
from math import log10


def count_digit(n):
    power = int(log10(n))
    return power + 1


if __name__ == "__main__":
    print(count_digit(4548767))
