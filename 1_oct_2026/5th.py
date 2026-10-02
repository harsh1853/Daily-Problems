#fidn teh nth term of a GP 
a = int(input("Enter the 1st term of GP : "))
b = int(input("Enter the 2nd term of GP : "))
n = int(input("Enter the nth term of the GP : "))
r = b//a
nth_term = a * (r ** (n - 1))
print(f"The nth term is {nth_term}")