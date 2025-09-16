def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm.
    """
    # Implement your solution here
    a1=max(a,b)
    b1=min(a,b)
    if b1==0:
        print("Error: Zero operand") 
        return None
    # Technically the gcd of 0 and n where n is positive is just n, 
    # but figured since you specified positive numbers only that you
    # would probably want this to throw an error. Otherwise, I would
    # include a check...
    # if b1==0
    #    return a1
    
    if b1<0:
        print("Error: Negative operand")
        return None
    r=a1%b1
    
    if not r:
        return b1
    return (gcd(b1,r))
