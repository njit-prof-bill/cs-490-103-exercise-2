def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two non-negative integers a and b
    using the Euclidean algorithm. Returns None for invalid input or negative numbers.
    """
    # Input validation
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None

    if a < 0 or b < 0:
        print("Error: Negative numbers are not allowed.")
        return None

    # Handle cases where either number is zero
    if a == 0 and b == 0:
        print("Error: GCD is undefined for a = 0 and b = 0.")
        return None
    if a == 0:
        return b
    if b == 0:
        return a

    # Recursive Euclidean algorithm
    if b == 0:
        return a
    return gcd(b, a % b)



print(gcd(48, 18))  
print(gcd(54, 24))  
print(gcd(101, 103))  
print(gcd(0, 5))  
print(gcd(7, 0))  
print(gcd(0, 0))  
print(gcd(-48, 18))  
print(gcd(48, -18))  
print(gcd(-48, -18))  
print(gcd(123456, 789012))  
print(gcd(12.5, 5))  
print(gcd("12", 6))  
