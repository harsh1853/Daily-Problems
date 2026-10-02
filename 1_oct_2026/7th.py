#Given a single integer n, your task is to find the sum of the
#  square of the first n odd natural Numbers.
n = int(input("Enter the number upto : "))
sum = 0
a = 1 
d = 2
nth_term = a + (n-1)*d
# print(nth_term)
for i in range (1,nth_term+1):
    if i%2 != 0:
        sum = sum + i**2
        # print(i)
print(sum)

#print first n odd number 

    
        
