def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """

    # Implement your solution here
    if (b < 0 or a < 0):
        return

    if (b > a):
        return gcd(b, a)
    
    if (b == 0):
        if (a == 0):
            return
        return a

    r = a%b
    a = b
    b = r
    if(b != 0):
        return gcd(a, r)
	
    return a
    pass

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
