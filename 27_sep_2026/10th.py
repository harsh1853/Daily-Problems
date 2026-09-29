#perfect square or not 
a = int(input("Enter the number to check : "))
# b = a*a
count = 0
for i in range (1,101):
    j = i*i
    if j == a:
        count = count + 1
if count == 1:
    print("Perfect square")
elif a == 0:
    print("Number entered is zero")
else:
    print("Not a perfect square")
