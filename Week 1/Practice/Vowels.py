x=input("Enter a word or phrase:")
y=x.lower().replace(" ", "")

u=0
z=0
for i in y:
    u+=1
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        z+=1
        

print("Number of vowels:",z)
print("Number of consonants:", u-z)
        