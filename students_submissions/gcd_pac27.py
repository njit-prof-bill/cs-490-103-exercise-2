def gcd(a: int, b: int) -> int:
    if a < b:
        return gcd(b, a)
    elif b < 0:
        return None
    elif b == 0:
        if a > 0:
            return a
        else:
            return None
    
    r = a % b
    if not r:
        return b
    else:
        return gcd(b, r)

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1