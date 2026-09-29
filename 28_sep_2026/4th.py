#Program for Sum of squares of first n natural numbers
a = int(input("Enter the number : "))
sum = 0 
for a in range (a,0,-1):
    sum = sum + a**2
print(sum)
