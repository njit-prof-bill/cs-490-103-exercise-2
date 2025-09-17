from typing import Optional

def gcd(a: int, b: int) -> Optional[int]:

    if not (type(a) is int and type(b) is int):
        print("Error: gcd expects two integers (not bool, float, or str).")
        return None

    # Handle the undefined case gcd(0, 0)
    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    a = -a if a < 0 else a
    b = -b if b < 0 else b

    # Base case
    if b == 0:
        return a
    return gcd(b, a % b)


# Tests
if __name__ == "__main__":
    print(gcd(48, 18))      
    print(gcd(101, 10))     
    print(gcd(-24, 54))    
    print(gcd(0, 7))   
    print(gcd(0, 0))    
    print(gcd(True, 5))    
    print(gcd(2.0, 4))      
