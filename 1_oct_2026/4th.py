#Given an integer n, Return an array containing the sum of odd numbers and even numbers from 1 to n,
#where the first number is the sum of odd numbers and the second number is the sum of even numbers.
n = int(input("Enter the number : "))
digit = []
sum_even = 0
sum_odd = 0
for i in range(1,n+1):
    digit.append(i)
print(digit)
for j in digit:
    if j%2==0:
        sum_even = sum_even + j
    else:
        sum_odd = sum_odd + j
print(f"{sum_odd} sum of odd numbers")
print(f"{sum_even} sum of even numbers")

