def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    if a < 0 or b < 0:
        print("Error: Negative Number")
        return None
    big=0
    small=0
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
    
    if small == 0:
        return big
    else:
        return gcd(small, big % small)

'''
print(gcd(7,2))
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(-3, 0))# negative
print(gcd(24,54))
print(gcd(7,23))
'''