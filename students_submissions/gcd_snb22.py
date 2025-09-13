def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Handle edge cases and errors
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both arguments must be integers")
        return None
    
    if a < 0 or b < 0:
        print("Error: Both arguments must be non-negative integers")
        return None
    
    if a == 0 and b == 0:
        print("Error: GCD of (0, 0) is undefined")
        return None
    
    # Base case: if one number is 0, the other is the GCD
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Recursive case: Euclidean algorithm
    return gcd(b, a % b)


print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(17, 13))  # Expected output: 1 (prime numbers)
print(gcd(100, 0))  # Expected output: 100 (one zero)
print(gcd(0, 25))  # Expected output: 25 (one zero)
print(gcd(-12, 8))  # Expected output: Error message and None (negative number)
print(gcd(15, -9))  # Expected output: Error message and None (negative number)
print(gcd(-18, -12))  # Expected output: Error message and None (both negative)
print(gcd(1, 1))  # Expected output: 1 (same numbers)
print(gcd(100, 50))  # Expected output: 50 (one divides the other)
print(gcd(7, 7))  # Expected output: 7 (identical numbers)
print(gcd(0, 0))  # Expected output: Error message and None