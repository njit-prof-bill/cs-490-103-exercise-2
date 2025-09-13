def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
# test cases
print(gcd(-12, 40))
print(gcd(48, 18))
print(gcd(101, 10))