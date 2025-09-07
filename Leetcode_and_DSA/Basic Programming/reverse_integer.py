"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


"""


import math


def reverse(x: int) -> int:

    MIN = -2147483648
    MAX = 2147483647

    ans = 0

    while x != 0:

        digit = int(math.fmod(x, 10))

        if (ans > int(MAX / 10)) or (
            ans == int(MAX / 10) and digit > int(math.fmod(MAX, 10))
        ):

            return 0

        if (ans < int(MIN / 10)) or (
            ans == int(MIN / 10) and digit < int(math.fmod(MIN, 10))
        ):

            return 0

        ans = (ans * 10) + digit

        x = int(x / 10)

    return ans


if __name__ == "__main__":
    print(reverse(4548767))
