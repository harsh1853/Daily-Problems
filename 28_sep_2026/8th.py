#calculator which will ask for operation in the sign itself
a = int(input("Enter the first number : "))
b = int(input("Enter the second number :"))
c = str(input("Enter the operation to be performed : "))
if c == '+':
    res = a+b
elif c == '-':
    res = a-b
elif c == '*':
    res = a*b
else:
    print(f"The operator {c} is invalid")
    res = None
if res is not None:
                print(f"The result is {res}")