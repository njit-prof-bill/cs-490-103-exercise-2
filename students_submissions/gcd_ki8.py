def gcd(a: int, b: int) -> int:
    return a if a < b else b


# Correct recursive implementation with edge case handling
def gcd_recursive(a: int, b: int) -> int:

    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: gcd expects two integers.")
        return None

    # Normalize to non-negative
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    if b == 0:
        return a

    return gcd_recursive(b, a % b)


# Test cases
print(gcd(54, 24))  # Expected output: 24
print(gcd(48, 18))  # Expected output: 18
print(gcd(101, 10))  # Expected output: 10
