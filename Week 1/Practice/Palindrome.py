a=input("Enter a name, phrase or sequence:")
b="".join(reversed(a.lower()))

if a.lower().replace(" ", "")==b.replace(" ", ""):
    print("It is a Palindrome")
else:print("It is not a Palindrome")