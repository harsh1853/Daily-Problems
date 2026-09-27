n1 = 572
r1 = n1 % 2
r2 = n1 % 4
r3 = n1 % 5
r4 = n1 % 8
r5 = n1 % 10
if (r1 == 0 and r2 == 0 and r3 ==0 and r4 == 0 and r5 == 0 ):
    print (f"{n1} is divisble by all the given number")
else:
    print("Not divisble by all numbers")


