def gcd(a: int, b: int) -> int:
    
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None

    a = abs(a)
    b = abs(b)

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test cases
print(f"gcd(54, 24) = {gcd(54, 24)}")
print(f"gcd(48, 18) = {gcd(48, 18)}")
print(f"gcd(101, 10) = {gcd(101, 10)}")
print(f"gcd(-54, 24) = {gcd(-54, 24)}")
print(f"gcd(54, -24) = {gcd(54, -24)}")
print(f"gcd(0, 5) = {gcd(0, 5)}")
print(f"gcd(5, 0) = {gcd(5, 0)}")
print(f"gcd(13, 17) = {gcd(13, 17)}")