a=int(input("Enter a number:"))

c=0
while a/10>=0:
    b=a%10
    c=c+b
    a=int(a/10)
    if a==0:
        break

print(c)    