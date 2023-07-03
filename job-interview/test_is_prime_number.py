def is_prime_number(n: int) -> bool:
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


# Test is_prime_number()
def test_is_prime_number():
    assert is_prime_number(2) is True
    assert is_prime_number(3) is True
    assert is_prime_number(5) is True
    assert is_prime_number(7) is True
    assert is_prime_number(11) is True
    assert is_prime_number(13) is True
    assert is_prime_number(17) is True
    assert is_prime_number(19) is True
    assert is_prime_number(23) is True
    assert is_prime_number(29) is True
    assert is_prime_number(31) is True
    assert is_prime_number(37) is True
    assert is_prime_number(41) is True
    assert is_prime_number(43) is True
    assert is_prime_number(47) is True
    assert is_prime_number(53) is True
    assert is_prime_number(59) is True
    assert is_prime_number(61) is True
    assert is_prime_number(67) is True
    assert is_prime_number(4) is False
    assert is_prime_number(44) is False
