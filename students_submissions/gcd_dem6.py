def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    # Alright let's get Euclidean
    
    # Handling negative numbers
    if a < 0 or b < 0:
        print("Negative numbers are invalid.")
        return None
    
    # We made it to 0!
    if a == 0:
        return b
    elif b == 0:
        return a
    
    # Swapping just to keep a > b
    if b > a:
        temp = a
        a = b
        b = temp
    
    # Recursive step
    return gcd(b, a%b)

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(7, 0)) # Expected output: 7
print(gcd(1, -1)) # Expected output: None + error msg
print(gcd(7, 11)) # Expected output: 1
