"""
Given a number x, determine whether the given number is Armstrong's number or not. A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

Here a, b, c and d are digits of input number abcd.....

Examples

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153

"""


def is_armstrong(n: int) -> bool:

    given = n
    sum = 0

    while n > 0:

        last_cube = (n % 10) ** 3

        sum = sum + last_cube

        n = n//10

    return given == sum


if __name__ == "__main__":
    print(is_armstrong(153))

    print(is_armstrong(152))
