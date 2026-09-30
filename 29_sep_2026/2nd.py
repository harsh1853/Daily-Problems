# a = int(input("Enter the number you want factorial of "))
# i = a-1
# while i>=1:
#     a = a*i
#     i = i-1
# print(a)
n = int(input("Enter the value : "))
r = int(input("Enter the value : "))
a = n-r
j = (n-r)-1
i = n-1
while i>=1:
    n = n*i
    i = i-1
while j>=1:
    a = a*j
    j = j-1
print(n/a)