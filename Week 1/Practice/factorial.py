i= 0

while i>=0 and i<10:
    i+=1
    fact=1
    for j in range (1, i+1):
        fact*=j
    print("Factorial of", i, ":", fact)
