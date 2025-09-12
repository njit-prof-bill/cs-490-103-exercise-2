def gcd(a: int, b: int) -> int:
    
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: Both inputs must be integers."

    if a < 0 or b < 0:
        return "Error: GCD is not defined for negative numbers."

    if a == 0 and b == 0:
        return "Error: GCD is undefined for a = 0 and b = 0."
    
    if b == 0:
        return a

    return gcd(b, a % b)

#Test Cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1