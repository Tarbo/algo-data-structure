# python3


def last_digit_of_fibonacci_number_naive(n):
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


def last_digit_of_fibonacci_number(n):
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
    a, b = 0, 1
    # Save only the last digit
    for num in range(n % 60):
        a, b = b, (a + b) % 10
    return a


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
