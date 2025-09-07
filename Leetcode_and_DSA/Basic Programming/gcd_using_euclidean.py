"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

"""


def gcd(x, y) -> int:

    while x > 0 and y > 0:

        if (x > y):

            x = x % y

        else:

            y = y % x

    if x == 0:

        return y

    else:

        return x


if __name__ == "__main__":

    nums = [2, 5, 6, 9, 10]

    mn = min(nums)
    mx = max(nums)
    print(gcd(mn, mx))
