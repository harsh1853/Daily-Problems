n = int(input("Enter the number you want factorial of : "))
fact = 1
count = 0 
for i in range(n-1,0,-1):
     n = n*i
fact = n
print(fact)
while fact > 0:
     fact % 10
     count = count + 1
     fact = fact//10
print(f"There are {count} digits in teh factorial")