#Given a positive integer n, return all the divisors of n in the ascending order.
a = int(input("Enter the number : "))
i = 1 
while i <= a:
    if a%i == 0:
        print(i)
    i = i+1
    
    