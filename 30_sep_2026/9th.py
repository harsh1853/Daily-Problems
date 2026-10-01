#A series with same common difference is known as arithmetic series. The first term of series is 'a' and common difference is d. 
# The series looks like a, a + d, a + 2d, a + 3d, . . . Find the sum of series upto nth term.
a = int(input("Enter the value of 1st term : "))
n = int(input("Enter the upto term : "))
d = int(input("Enter the common difference : "))
nth_term = a + (n-1)*d
# for i in range (a,(nth_term + 1))
print(nth_term)
i = a
sum = 0 
while i <= nth_term:
    sum = sum + i
    # print(i)
    i = i + d
print(sum)

