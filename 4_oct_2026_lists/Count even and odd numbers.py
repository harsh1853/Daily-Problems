n = int(input("Enter the number of element : "))
l = []
c_even = 0
c_odd = 0
for i in range (n):
    x = int(input("Enter the number : "))
    l.append(x)
print(l)

for j in l:
    if j % 2 == 0:
        c_even = c_even + 1
    else:
        c_odd = c_odd + 1
print(c_odd)
print(c_even)
