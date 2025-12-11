def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive).
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("gcd expects two integers")

    # Ensure non-negative values
    a, b = abs(a), abs(b)

    # Base case
    if b == 0:
        return a

    # Recursive step
    return gcd(b, a % b)


# Test cases
print(gcd(54, 24))    # Expected 6
print(gcd(48, 18))    # Expected 6
print(gcd(101, 10))   # Expected 1
print(gcd(-36, 60))   # Expected 12
print(gcd(0, 25))     # Expected 25
print(gcd(0, 0))      # Expected 0 (convention, though mathematically undefined)

