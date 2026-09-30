n = int(input("Enter the value : "))
r = int(input("Enter the value : "))
a = (n-r)
d = a-1
b = n-1
c = r-1
while b >= 1:
    n = n*b
    b = b-1
print(f"Factorial is {n}")
while c >= 1:
    r = r*c
    c = c-1
print(f"Factorial is {r}")
while d >= 1:
    a = d*a
    d = d-1
print(f"Factoria is {a}")
print(n/(r*a))

