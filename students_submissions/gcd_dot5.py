def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: Inputs must be integers.")
        return None

    a, b = abs(a), abs(b)

    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None
    if b == 0:
        return a

    return gcd(b, a % b)

if __name__ == "__main__":
    print("gcd(48, 18) =", gcd(48, 18))    # Expected 6
    print("gcd(7, 13) =", gcd(7, 13))      # Expected 1 (prime numbers)
    print("gcd(-27, 36) =", gcd(-27, 36))  # Expected 9 (handles negatives)
    print("gcd(0, 5) =", gcd(0, 5))        # Expected 5
    print("gcd(0, 0) =", gcd(0, 0))        # Expected None (error case)
    print("gcd(20, 'a') =", gcd(20, "a"))  # Expected None (invalid input)

