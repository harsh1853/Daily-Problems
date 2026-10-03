#Given an integer n, return all the divisors of n in the ascending order.
n = int(input("Enter the number : "))
for i in range(1,n+1):
    if n%i == 0:
        print(i)