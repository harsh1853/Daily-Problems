#prime number by count method 
a = int(input("Ente rthe number : "))
count = 0 
for i in range (1,a+1):
    if a%i == 0:
        count = count + 1
if count > 2:
    print(f"{a} is not a prime number ")
elif a == 0:
    print("The number enter is zero neither prime not composite")
else:
    print(f"{a} is a prime number")

