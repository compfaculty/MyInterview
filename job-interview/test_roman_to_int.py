def roman_to_int(roman_number: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    roman_len = len(roman_number)
    i = 0
    while True:
        if i + 1 > roman_len:
            break
        if i + 1 == roman_len:
            num += roman[roman_number[-1]]
            break
        cur = roman_number[i]
        nxt = roman_number[i + 1]
        if cur == 'I' and nxt in ('V', 'X'):
            num += roman[nxt] - 1
            i += 2
            continue
        if cur == 'X' and nxt in ('L', 'C'):
            num += roman[nxt] - 10
            i += 2
            continue
        if cur == 'C' and nxt in ('D', 'M'):
            num += roman[nxt] - 100
            i += 2
            continue
        num += roman[cur]
        i += 1

    return num


def test_roman_to_int():
    assert roman_to_int("I") == 1
    assert roman_to_int("II") == 2
    assert roman_to_int("III") == 3
    assert roman_to_int("XV") == 15
    assert roman_to_int("XVI") == 16
