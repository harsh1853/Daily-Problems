n = int(input("Enter how many number : "))
t = []
for i in range (n):
    x = int(input("Enter the number : "))
    t.append(x)
print(tuple(t))
print(tuple(reversed(t)))
