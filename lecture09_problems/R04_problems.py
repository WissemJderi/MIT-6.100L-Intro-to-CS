# Problem 1: Lamba Functions Practice
# a) Write a lambda function that calculates the cube root of a given number
# passed in as an argument
# INSERT CODE BELOW HERE
f1 = lambda x: x ** (1 / 3)

# b) Write a lambda function that takes in two arguments and outputs the product
# of those two numbers.
# INSERT CODE BELOW HERE
f2 = lambda x, y: x * y

# uncomment to test function
print(f1(8))
print(f1(4))
print(f2(1, 2))
print(f2(4, 5))


#############################################################################
# Problem 2: Practice working with Tuples:
# Write a function that counts the number of times the number 1 appears
# in an inputted tuple.
# INSERT CODE BELOW HERE


def count_number_one(nums):
    counter = 0
    for num in nums:
        if num == 1:
            counter += 1
    return counter


# uncomment to test function
print(count_number_one((1, 2, 3, 4, 5, 1, 1)))


#############################################################################
# Problem 3: Practice working with Python Tuples
# Write a Function that takes in two tuples and outputs a single tuple containing
# only common elements of both tuples.
# INSERT CODE BELOW HERE
def common_elements(tup1, tup2):
    output = ()
    for num in tup1:
        if num not in output:
            output += (num,)
    for num in tup2:
        if num not in output:
            output += (num,)
    return output


# uncomment to test function
print(common_elements((2, 3, 4), (3, 4, 5, 6)))
