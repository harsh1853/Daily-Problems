#Find the smallest element
n = int(input("Enter the number of element : "))
l = []
for i in range (n):
    x = int(input("Enter the number : "))
    l.append(x)
l.sort()
print(f"The smallest elemet is {l[0]}")
