def gcd(a: int, b: int) -> int:
    if a == 0 and b == 0:
        print("Error: A and B == 0")
        return None
    elif a < 0 and b < 0: 
        print("Error: A and B are negative, please enter positive numbers.")
        return None
    elif b == 0:
        return a

    return gcd(b, a % b)

if __name__ == "__main__":
    print(gcd(54, 24))
    print(gcd(48, 18))
    print(gcd(101, 10))
    print(gcd(13, 17))
    print(gcd(-54, 24))
    print(gcd(101, 10)) 
    print(gcd(48,18))