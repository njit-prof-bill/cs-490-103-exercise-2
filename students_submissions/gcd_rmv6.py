def gcd(a: int, b: int) -> int:
    if a<0 or b<0:
        print("Error a number is negative.")
        return None
    
    if a==1:
        print("Error a number is prime.")
        return None
    
    if b==0 and a!=0:
        return a
    
    if a==0 or b==0:
        print("Error a number is 0.")
        return None

    else:
        return gcd(b, a % b)
    


# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Return None prime number
print(gcd(-5, 10))  #return None negative number
print(gcd(3, -4)) # return None negative number
print(gcd(0, 10)) # return None 0