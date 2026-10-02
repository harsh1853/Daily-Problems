#Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.
n = int(input("Enter the number : "))
sum = 0 
for i in range (1,n+1):
    sum = sum + i**3
print(sum)