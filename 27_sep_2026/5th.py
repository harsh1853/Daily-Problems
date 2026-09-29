#power and bases using the logic and not predefined functions
m = int(input("Enter the base value : "))
n = int(input("Enter the power value : "))
i = 1
j = 1 
while i <= n:
    j = j*m
    i = i+1
print(j)