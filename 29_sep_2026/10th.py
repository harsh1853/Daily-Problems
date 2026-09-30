# Given two integers n and m (m != 0). The problem is to find the number closest to n and divisible by m. If there is more than one such number, 
# then output the one having the maximum absolute value.
n = int(input("Enter the number to be divided : "))
m = int(input("Enter the number with which division is to be performed "))
div_list = []
fin_list = []
for i in range (0,100):
    if i%m == 0:
        div_list.append(i)
print(div_list)
for j in div_list:
    if n >= j:
        fin_list.append(j)
print(fin_list)
print(fin_list[-1])

        