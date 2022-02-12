# python3


def fibonacci_number_naive(n: int) -> int:
    """
        Naive fibonnacci algorithm with recursion
    Args:
        n (int): Number of fibonacci sequence

    Returns:
        Value of the n-th fibonacci sequence
    """
    assert 0 <= n <= 45
    print("Compute F sub", n)
    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    """
        Efficient fibonacci algorithm implementation.
    Args:
        n (int): Number of Fibonacci sequence.

    Returns:
        The n-th fibonacci sequence.
    """
    assert 0 <= n <= 45

    if n <= 1:
        return n
    f_numbers = [0] * n
    # Assign the f(0) and f(1)
    f_numbers[1] = 1
    for num in range(2, n):
        f_numbers[num] = f_numbers[num - 1] + f_numbers[num - 2]
    return f_numbers[n-1]+f_numbers[n-2]


if __name__ == '__main__':
    input_n = int(input())
    # print(fibonacci_number_naive(40))
    print(fibonacci_number(input_n))
