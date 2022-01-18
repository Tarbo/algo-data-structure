# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    # Get the index of the maximum number.
    index_i = -1
    for i in range(len(numbers)):
        if (numbers[index_i] < numbers[i]) | (index_i == -1):
            index_i = i
    # Get the index of the second max number.
    index_j = -1
    for j in range(len(numbers)):
        if (j != index_i) and (numbers[index_j] < numbers[j]) | (index_j == -1):
            index_j = j
    return numbers[index_j] * numbers[index_i]


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
