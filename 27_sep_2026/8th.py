#fibonacci series 
n1 = 0
n2 = 1
print(n1, end = ",")
print(n2, end = ",")
for i in range (13):
    next = n1 + n2
    print(next,end = ",")
    n1 = n2
    n2 = next

