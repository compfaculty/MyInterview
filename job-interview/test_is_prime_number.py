from pytest_benchmark.plugin import benchmark


def is_prime_numberV1(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_numberV2(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_prime_numbers(n):
    count = 0
    num = 2

    while count < n:
        if is_prime_numberV2(num):
            yield num
            count += 1
        num += 1


def generate_non_prime_numbers(n):
    count = 0
    num = 0

    while count < n:
        if not is_prime_numberV2(num):
            yield num
            count += 1
        num += 1


# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
primes = list(generate_prime_numbers(10000))
non_primes = list(generate_non_prime_numbers(10000))


def test_is_prime_number_v1():
    for num in primes:
        assert is_prime_numberV1(num) is True

    for num in non_primes:
        assert is_prime_numberV1(num) is False


def test_is_prime_number_v2():
    for num in primes:
        assert is_prime_numberV2(num) is True

    for num in non_primes:
        assert is_prime_numberV2(num) is False


def test_is_prime_number_benchmark1(benchmark):
    benchmark(test_is_prime_number_v1)


def test_is_prime_number_benchmark2(benchmark):
    benchmark(test_is_prime_number_v2)
