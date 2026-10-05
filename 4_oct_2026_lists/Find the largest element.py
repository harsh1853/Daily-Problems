n = int(input("How many elements : "))
l = []
for i in range (n):
    x = int(input("Enter the number : "))
    l.append(x)
print(l)
l.sort()
print(f"The max elemet is {l[-1]}")