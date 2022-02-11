"""
     Euclidean common divisor algorithm.
"""


def greatest_common_divisor(num_a: int, num_b: int) -> int:
    """
        A method to compute the greatest common divisor.
    Args:
        num_a (int): The first number.
        num_b (int): Second number

    Returns:
        The greatest common divisor.
    """
    if num_b == 0:
        return num_a
    print(f">>> Value of num_b: {num_b}")
    return greatest_common_divisor(num_b, num_a % num_b)


if __name__ == "__main__":
    a = 357
    b = 234
    print(f">>> GCD of {a} and {b} is: {greatest_common_divisor(a, b)}")
