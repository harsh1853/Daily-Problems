#Given a number n, find the digital root of n. Digital Root of a number is the recursive sum of its digits until we get a single digit number.
a = int(input("Enter the number : "))
i = 0
count = 0 
while a > 0:
    i = i + a%10
    count = count + 1
    a = a//10
# print(i)
sum = 0
while i > 0:
    sum = sum + i%10
    i = i//10
print(sum)

