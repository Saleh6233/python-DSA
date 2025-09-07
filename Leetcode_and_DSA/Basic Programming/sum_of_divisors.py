"""
Find the number of divisors and sum of divisors of number n

"""


def sum_of_divisors(n: int) -> int:

    i = 1
    sum = 0

    while i <= n:

        if (n % i == 0):

            sum = sum + 1

        i = i+1

    return sum


if __name__ == "__main__":
    print(sum_of_divisors(153))

    print(sum_of_divisors(152))
