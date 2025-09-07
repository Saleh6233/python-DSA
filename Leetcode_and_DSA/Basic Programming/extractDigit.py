"""
Given a number N, the task is to write a python program to print all digits of the number N in their original order. Examples:

Input: N = 12
Output: 1, 2 

Input: N = 1032
Output: 1, 0, 3, 2

"""


def showDigit(n):
    extract_digit = []
    if n == 0:
        return [0]
    if n < 0:
        n = -n

    while n > 0:
        last = n % 10
        extract_digit.append(last)
        n = n // 10

    extract_digit.reverse()
    return extract_digit


if __name__ == "__main__":
    n = 3452897
    print(*showDigit(n), sep=", ")
