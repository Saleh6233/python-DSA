"""
A prime number is a positive integer that is divisible only by 1 and itself. For example: 2, 3, 5, 7, 11, 13, 17. Now check whether the given number is a prime number or not.

Examples:

Input: n = 29
Output: 29 is Prime
Explanation: 29 has no divisors other than 1 and 29 itself. Hence, it is a prime number.

Input: n = 15
Output: 15 is NOT prime
Explanation: 15 has divisors other than 1 and 15 (i.e., 3 and 5). Hence, it is not a prime number.

"""

import math


def is_prime_number(n: int) -> bool:

    if n <= 1:
        return False

    i = 1
    count = 0
    root_sqrt = int(math.sqrt(n))

    while i <= root_sqrt:

        if (n % i == 0):

            count = count + 1

            if (int(n / i) != i):

                count = count + 1

        i = i+1

    return count == 2


if __name__ == "__main__":
    print(is_prime_number(29))

    print(is_prime_number(15))
