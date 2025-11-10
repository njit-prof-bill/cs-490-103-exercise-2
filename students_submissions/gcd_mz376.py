def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    try:
        int_a = int(a)
        int_b = int(b)
    except Exception:
        print("Both inputs must be integers.")
        return None
    
    if a==0 and b==0:
        print("GCD is not defined for both numbers being zero.")
        return None
    
    a, b = abs(int_a), abs(int_b)

    return a if b == 0 else gcd(b, a % b)

# Example usage:
if __name__ == "__main__":
    print(gcd(48, 18))  # Output: 6
    print(gcd(-48, 18)) # Output: 6
    print(gcd(48, -18)) # Output: 6
    print(gcd(0, 0))    # Output: GCD is not defined for both numbers being zero.
    print(gcd(0, 5))    # Output: 5
    print(gcd(5, 0))    # Output: 5
    print(gcd("a", 5))  # Output: Both inputs must be integers.