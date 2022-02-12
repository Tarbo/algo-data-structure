# python3


def last_digit_of_fibonacci_number_naive(n: int):
    """
        A naive method provided by coursera.
    Args:
        n (int):

    Returns:

    """
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n: int) -> int:
    """
        A method to retrieve the last digit of fibonacci numer
    Args:
        n (int):

    Returns:
        Returns the last digit of fibonacci sequence
    """
    assert 0 <= n <= 10 ** 7
    if n <= 1:
        return n
    f_numbers = [0] * n
    # Assign the f(0) and f(1)
    f_numbers[1] = 1
    for num in range(2, n):
        f_numbers[num] = f_numbers[num - 1] + f_numbers[num - 2]
    return (f_numbers[n - 1] + f_numbers[n - 2]) % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
