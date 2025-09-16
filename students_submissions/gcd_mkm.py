def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Both numbers must be integers")
        return None
    
    a = abs(a)
    b = abs(b)

    if(b>a):
        temp=b
        b=a
        a=temp

    if a == 0:
        return b
    if b == 0:
        return a

    if(a % b != 0):
        return (gcd(a % b, b))
    return b