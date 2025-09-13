def gcd(a: int, b: int) -> int:
    if b == 0:
        return abs(a) 
    return gcd(b, a % b)
