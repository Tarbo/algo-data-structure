"""
     Euclidean common divisor algorithm.
"""


def greatest_common_divisor(a: int, b: int) -> int:
    """
        A method to compute the greatest common divisor.
    Args:
        a (int): The first number.
        b (int): Second number

    Returns:
        The greatest common divisor.
    """
    if b == 0:
        return a
    print(f">>> Value of b: {b}")
    return greatest_common_divisor(b, a % b)


if __name__ == "__main__":
    a = 357
    b = 234
    print(f">>> GCD of {a} and {b} is: {greatest_common_divisor(a, b)}")
