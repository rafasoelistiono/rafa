def gcd(a, b):
    while b != 0:
        sisa = a % b
        a = b
        b = sisa
    return a   

print(gcd(12,7))
    
