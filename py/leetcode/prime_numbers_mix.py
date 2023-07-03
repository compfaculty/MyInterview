import timeit


def func_prime(n: int) -> bool:
    # Use a breakpoint in the code line below to debug your script.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def benchmark():
    print(timeit.timeit("func_prime(9999999999)", "from __main__ import func_prime", number=1))


if __name__ == '__main__':
    benchmark()
