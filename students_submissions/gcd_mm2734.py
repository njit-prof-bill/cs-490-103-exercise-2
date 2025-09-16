def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive; no loops).
    Returns None if input is invalid.
    """

    # Validate inputs
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: gcd expects two integers.")
        return None

    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    # Work with absolute values so negatives don’t break logic
    a, b = abs(a), abs(b)

    # Base case
    if b == 0:
        return a

    # Recursive step
    return gcd(b, a % b)


# ------------------------
# Basic test cases
# ------------------------
if __name__ == "__main__":
    print(gcd(54, 24))    # Expected output: 6
    print(gcd(48, 18))    # Expected output: 6
    print(gcd(101, 10))   # Expected output: 1
    print(gcd(-42, 56))   # Expected output: 14
    print(gcd(0, 15))     # Expected output: 15
    print(gcd(0, 0))      # Expected output: Error + None