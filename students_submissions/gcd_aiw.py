def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.

    """

    # Implement your solution here

    big = max(a,b)
    small = min(a,b)
    
    if small == 0:
        return big

    if big < 0 or small < 0:
        print ("invalid result. Result must be greater than or equal to 0.")
        return None
    
    if big % small == 0:
        return small
    

    return gcd(small,big%small)

