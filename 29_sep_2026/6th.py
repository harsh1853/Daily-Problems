# K-th digit in 'a' raised to power 'b'
# Given three numbers a, b and k, find k-th digit in ab from right side
a = int(input("Enter the base : "))
b = int(input("Enter the power : "))
k = int(input("Enter the value of K "))
c = a**b
# print(c)
if k == 1:
    m = c%10
    print(m)
if k == 2:
    m = c//10
    print(m)
    
           

        





    