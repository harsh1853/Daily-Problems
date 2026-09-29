#calculator by asking for input by user 
a = int(input("Enter the first number : "))
b = int(input("Enter teh second number : "))
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
c = int(input("Which operation to perform : "))
if c == 1:
    res = a+b
elif c == 2:
    res = a-b
elif c == 3:
    res = a*b
else:
    res = None
if res == None:
    print("Please enter appropriate option")
print(f"The result is {res}")



