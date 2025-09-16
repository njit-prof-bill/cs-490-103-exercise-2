def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive, no loops).
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None

    a, b = abs(a), abs(b)

    if b == 0:
        return a

    return gcd(b, a % b)


# --- Test cases ---
if __name__ == "__main__":
    print(gcd(54, 24))   # Expected output: 6
    print(gcd(48, 18))   # Expected output: 6
    print(gcd(101, 10))  # Expected output: 1
    print(gcd(-20, 30))  # Expected output: 10
    print(gcd(0, 5))     # Expected output: 5
    print(gcd(0, 0))     # Expected output: 0 (edge case)
