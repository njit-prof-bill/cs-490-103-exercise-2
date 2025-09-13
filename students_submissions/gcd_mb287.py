def gcd(a:int,b:int)->int:
    if a==0 and b==0:
        print("Error: gcd(0,0) is undefined")
        return None

    a, b=abs(a),abs(b)
    if b==0:
        return a
    return gcd(b,a%b)


#Tests
print(gcd(54,24))    
print(gcd(48,18))    
print(gcd(101,10))   
print(gcd(-42,56))   
print(gcd(0,5))      
print(gcd(0,0))     
