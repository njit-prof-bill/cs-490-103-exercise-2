def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive).
    """

    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both inputs must be integers.")
        return None
    

    a, b = abs(a), abs(b)
    
    if b == 0:
        return a
    return gcd(b, a % b)



print(gcd(54, 24))  
print(gcd(48, 18))   
print(gcd(101, 10)) 
print(gcd(-42, 56))  
print(gcd(0, 0))     
