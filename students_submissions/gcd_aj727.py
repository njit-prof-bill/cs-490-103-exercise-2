def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive).
    """
    # Handle invalid input
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    
    # Convert to positive (GCD is always positive)
    a, b = abs(a), abs(b)
    
    # Base case
    if b == 0:
        return a
    return gcd(b, a % b)


# ✅ Test cases
print(gcd(54, 24))   # Expected 6
print(gcd(48, 18))   # Expected 6
print(gcd(101, 10))  # Expected 1
print(gcd(-42, 56))  # Expected 14
print(gcd(0, 0))     # Edge case: returns 0
