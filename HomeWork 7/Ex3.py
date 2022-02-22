def is_perfect(n: int):
    sum = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            sum += i
    if n == sum:
        return True
    else:
        return False


# print(is_perfect(28))


def perfect_numbers(n: int):
    numbers_list = []
    m = 2
    while m > 1 and len(numbers_list) < n:
        if is_perfect(m):
            numbers_list.append(m)
        m += 2
    return numbers_list


# print(perfect_numbers(4))
