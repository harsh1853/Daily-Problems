n = int(input("How many digits "))
l = []
for i in range(n):
    x = int(input("Enter the number : "))
    l.append(x)
print(l[::-1]) #print(l[-1:(-(len(l))-1):-1])