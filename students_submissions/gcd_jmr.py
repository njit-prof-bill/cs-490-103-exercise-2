def gcd(a: int, b: int) -> int:
    if a == 0 and b == 0:
        print("Error GCD is undefined")
        return None
    a, b = abs(a), abs(b)
    # Base 
    if b == 0:
        return a
    return gcd(b, a % b)

    return a if a < b else b


# Test cases
print(gcd(54, 24))  # Expected output: 24
print(gcd(48, 18))  # Expected output: 18
print(gcd(101, 10))  # Expected output: 10
