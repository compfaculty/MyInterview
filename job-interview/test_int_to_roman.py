from pytest_benchmark.plugin import benchmark


def int_to_roman(number):
    if 0 > number > 3999:
        raise ValueError('should be in  0 .. 3999 : {}'.format(number))
    to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                2000: 'MM', 3000: 'MMM'}
    count = 1
    res = []
    for digit in str(number)[::-1]:
        if digit != '0':
            res.append(to_roman[int(digit) * count])
        count *= 10
    return "".join(reversed(res))


def test_solution():
    assert int_to_roman(5) == 'V'
    assert int_to_roman(6) == 'VI'
    assert int_to_roman(7) == 'VII'
    assert int_to_roman(3000) == 'MMM'
