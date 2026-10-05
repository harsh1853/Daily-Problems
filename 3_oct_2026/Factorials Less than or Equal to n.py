n = int(input("Enter the number : "))
fact1 = []
fact = 1
for i in range (1,n+1):
    fact = fact*i
    fact1.append(fact)
for j in fact1:
    if n >= j:
        print(j)

