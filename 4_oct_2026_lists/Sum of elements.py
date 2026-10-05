n = int(input("How many number : "))
l = []
sum = 0
for i in range (n):
    x = int(input("Enter the number :"))
    l.append(x)
print(l)
for j in l:
    sum = sum + j
print(sum)
