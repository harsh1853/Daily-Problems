#factorial number using while loop 
a = int(input("Enter the number you want the factorial of : "))
i = a-1
while i>=1:
    a = a*i
    i = i-1
print(a)