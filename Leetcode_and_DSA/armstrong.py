def is_armstrong(n: int) -> bool:

    given = n
    sum = 0

    while n > 0:

        last_cube = (n % 10) ** 3

        sum = sum + last_cube

        n = int(n/10)

    return given == sum


if __name__ == "__main__":
    print(is_armstrong(153))

    print(is_armstrong(152))
