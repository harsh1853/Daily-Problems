#Given a positive integer n, The task is to find the value of Σi F(i) where i is 
# from 1 to n and function F(i) is defined as the sum of all divisors of i.
n = int(input("Enter the number : "))
sum = 0
for i in range (1,n+1):
    # print(i)
    for j in range (1,i+1):
        if i%j == 0:
            sum = sum + j
print(sum)