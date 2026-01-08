a=int(input("Enter an integer:"))

for i in range (2,a):
    if a%i==0:
        print("Number is composite")
        exit() # or quit() , sys,exit() more professional
print("Number is prime")