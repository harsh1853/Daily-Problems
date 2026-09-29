#factorial number using for loop
a = int(input("Enter the number you want the factorial of : "))
for i in range (a-1,0,-1):
    a = a*i
print(a)