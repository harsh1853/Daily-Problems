#Grade calculator 
a = float(input("Enter your Physics marks : "))
b = float(input("Enter your Chemistry marks : "))
c = float(input("Enter your Mathematics marks : "))
d = float(input("Enter your Biology marks "))
e = (a+b+c+d)/4
print(f"The average mark is {e} ")
if e <= 100 and e >= 80:
    print("Grade A")
elif e < 80 and e >= 60:
    print("Grade B")
elif e < 60 and e >= 40:
    print("Grade C")
elif e < 40 and e >= 35:
    print("Grade D")
else:
    print("Failed")
