# accept the input in a list and then convert that list into a tuple by type_casting

n = int(input("Enter the number of element : "))
l = []
for i in range (n):
    x = int(input("Enter the number : "))
    l.append(x)
print(tuple(l))
 
# Alternative way
 
# n = tuple(map(int , input("Enter the data : ").split()))
# print(n)