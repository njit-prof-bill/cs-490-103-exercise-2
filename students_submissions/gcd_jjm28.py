def gcd(a, b):
    # Implement your solution here
    if a == 0 and b == 0:
        print("print the values given are undefined")
        return

    a,b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd(b , a % b)

print(gcd(0,0))
print(gcd(-48,18))
print(gcd(54,24))
print(gcd(101,10))