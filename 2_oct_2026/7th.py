#A Strong Number is a number whose value is equal to the sum of the factorials of its digits.\
n = int(input("Enter the number : "))
original_number = n 
l1 = []
sum = 0
while n > 0:
    k = n%10
    n = n//10
    l1.append(k)
print(l1)
for i in l1:
    fact = 1
    for j in range(1,i+1):
        fact = fact*j
    sum = sum + fact
    print(f"Factorial of {i} is {fact}")
if sum == original_number:
    print("Strong Number")
else:
    print("Not a strong number")
    