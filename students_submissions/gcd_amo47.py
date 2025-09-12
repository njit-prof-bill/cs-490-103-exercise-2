def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here

    if a == 0 and b == 0:
        print("GCD does not exist")
        return None

    if a == 0 or b == 0:
        return a if a != 0 else b
    
    # For negative values
    a = abs(a)
    b = abs(b)

    new_a = b
    new_b = a % b
    return gcd(new_a, new_b)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1