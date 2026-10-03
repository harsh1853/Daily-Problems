#Given a number n, check if the number is perfect or not. A number is said to be 
# perfect if sum of all its factors excluding the number itself is equal to the number.
n = int(input("Enter the number : "))
sum = 0
for i in range (1,n):
    if n%i == 0:
        sum = sum + i
if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")


