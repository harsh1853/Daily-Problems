# find the roots of the squadratic equation 
a = int(input("Enter the coefficint of x square : "))
b = int(input("Enter the coefficint of only x : "))
c = int(input("Enter the value of the constant : "))
print(f"The equation is : {a}x**2 + ({(b)}x) + c")
d = ((b*b)-4*a*c)**1/2
print(f"The determinant is {d} ")
root1 = ((-b)+d)/(2*a)
root2 = ((-b)-d)/(2*a)
print(f"The roots of the equation is {root1} and {root2}")