def gcd(a: int, b: int) -> int :
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("Please enter in only Integers for this method")
        exit(1)
    a, b = abs(a), abs(b)
    
    if b == 0:          
        return a
    if a < b:            
        a, b = b, a
    return gcd(b, a % b)

        

print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
