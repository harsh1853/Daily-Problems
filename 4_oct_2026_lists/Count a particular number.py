#Count a particular number
n = int(input("Enter the number of elemet : "))
l = []
c = 0
for i in range (n):
    x = int(input("Enter the numbers : "))
    l.append(x)
num = int(input("Enter the number you looking for : "))
for j in l:
    if j == num:
        c = c + 1
print(c)
