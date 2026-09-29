#reversing a number 
a = int(input("Enter the number : "))
digit = 0 
while a > 0:
    digit = a%10
    print(digit, end = "")
    a = a//10