def gcd(a,b):
    while(b):
        a,b = b,a%b
    return a
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
result = gcd(num1,num2)
print(f"the gcd of",num1,"and",num2,'is',result)
output:
enter the first number:46
enter the second number:12
the gcd of 46 and 12 is 2
