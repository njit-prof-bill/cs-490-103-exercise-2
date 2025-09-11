def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None

    # Special undefined case
    if a == 0 and b == 0:
        print("Error: GCD is undefined for a = 0 and b = 0.")
        return None

    # Always work with absolute values (GCD is non-negative)
    a, b = abs(a), abs(b)

    # Base cases
    if b == 0:
        return a
    if a == 0:
        return b

    # Recursive case
    return gcd(b, a % b)
    

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
    