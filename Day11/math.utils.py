
def is_prime(n: int) -> bool:
    """Check whether a number is prime."""
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Number cannot be negative")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""
    while b != 0:
        a, b = b, a % b

    return abs(a)


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    if n < 0:
        raise ValueError("n cannot be negative")

    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


print("Prime:", is_prime(7))
print("Factorial:", factorial(5))
print("GCD:", gcd(12, 18))
print("LCM:", lcm(4, 6))
print("Fibonacci:", fibonacci(7))
