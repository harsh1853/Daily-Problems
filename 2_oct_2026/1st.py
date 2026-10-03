#Given two positive integers a and b, find GCD of a and b.
#Self but partial approach
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
j = 1
# for i in range (1,1000):
#     if a%i == 0 and b%i == 0:
#         j = i
# print(j)
for i in range(1,(min(a,b)+1)):
    if a%i == 0 and b%i == 0:
        j = i 
print(j)
    
        