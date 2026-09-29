#check if the number is divisble by a number completely 
m = int(input("Enter the Denumerator : "))
n = int(input("Enter the Numerator : "))
if m%n == 0:
    print(f"{m} is completely divisible by {n} ")
else:
    print("Not completely divisible")