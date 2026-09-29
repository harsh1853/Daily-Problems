#extracting digits and squaring the sum of the digits in a number 
a = int(input("Enter the number : "))
digit = 0 
sum = 0
while a > 0:
    digit = a%10
    a = a//10
    sum = sum + digit**2  
print(sum)
