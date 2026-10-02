#Given two integers n and m (m != 0). The problem is to find the number closest to n 
# and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.
#partially correct
n = int(input("Enter the value : "))
m = int(input("Enter the value : "))
# mul = []
# mul1 = []
# for i in range (1,11):
#     # print(i*n)
#     mul.append(i*m)
# print(mul)
# for j in mul:
#     if n > j:
#         mul1.append(j)
# print(mul1[-1])
lower = (n//m)*m
upper = lower + m
if abs(n - lower) < abs(n - upper):
    print((lower))
else:
    print(abs(upper))
