def gcd(a: int, b: int) -> int:
    
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Inputs must be integers.")
        return None

    # handling both values being zero
    if a == 0 and b == 0:
        print("Error: GCD is undefined for a = 0 and b = 0.")
        return None

    # making numbers positive
    a, b = abs(a), abs(b)

    # base case
    if b == 0:
        return a

    # recursive case
    return gcd(b, a % b)


# test cases
print(gcd(54, 24))
print(gcd(48, 18))
print(gcd(101, 10))
print(gcd(-54, 24))
print(gcd(0, 5))
print(gcd(0, 0))
print(gcd("a", 10))
 
