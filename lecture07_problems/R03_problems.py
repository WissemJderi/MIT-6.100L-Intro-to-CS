# Problem 1 - Bisection Search Practice
# Write a program using bisection search to find the forth root of a number inputted by the
# user. Print the forth root calculated with max error of 0.01.

# x = float(input("Using bisection search calculate the forth root of: " ))
# epsilon = 0.01
# low = 0
# high = x
# ans = (low + high) / 2

# while abs(ans ** 4 - x) > epsilon:
#     if ans ** 4 > x:
#         high = ans
#     else:
#         low = ans
#     ans = (low + high) / 2
# print(ans)


# Problem 2 - Functions
# Write a Python function to check whether a number falls in a given range.
# def in_the_range(num, rang_start, rang_end):
#     return num >= rang_start and num <= rang_end

# print(in_the_range(6, 3, 9))



# Problem 3 - Functions
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal
# to the sum of its proper positive divisors, excluding the number itself).
def is_perfect_num(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num


print(is_perfect_num(28))
