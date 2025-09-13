
def gcd(a: int, b: int) -> int:

    # Check if inputs are valid integers
    if not isinstance(a, int) or not isinstance(b, int):
        print("ERROR, inputs must be integers.")
        return None
    
    # Check if inputs are positive, nonzero integers
    if a < 0 or b < 0:
        print("ERROR, inputs must be POSITIVE integers.")
        return None
    
    # Check if both are zero
    if a == 0 and b == 0:
        print("ERROR, GCD is undefined for a = 0 and b = 0.")
        return None
    
    # Check for prime numbers
    if a == 1:
        print("ERROR, Prime numbers don't have GCD.")
        return None
    
    
    # Ecludiean Algorithm using recursive method
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1 (Prime number)
print(gcd(2, 18))  # Expected output: 2
print(gcd(5, 50))  # Expected output: 5
print(gcd(90, 9))  # Expected output: 9

print(gcd(1, 17))  # Expected output: 1 because of prime numbers
print(gcd(-1, 17))  # Expected output: error cause of negative number
print(gcd(0, 0))  # Expected output: error cause of zero in both inputs


