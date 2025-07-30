# Problem 1: Given a list of numbers. Write a function to turn every item of
# a list into its square.
def square_list(my_list):
    for i in range(len(my_list)):
        my_list[i] = my_list[i] ** 2
    return my_list


# test
# print(square_list([1, 2, 3, 4]))
# print(square_list([10, 12, 13]))


# Problem 2: Write a Python program to concatenate element-wise
# three given lists of same length
# Original lists:
list1 = ["0", "1", "2", "3", "4"]
list2 = ["red", "green", "black", "blue", "white"]
list3 = ["100", "200", "300", "400", "500"]
# Expected output : ['0red100', '1green200', '2black300', '3blue400', '4white500']


def concatenate_lists(list_a, list_b, list_c):
    new_list = []
    for i in range(len(list_a)):
        new_list.append(list_a[i] + list_b[i] + list_c[i])

    return new_list


# test
# print(concatenate_lists(list1, list2, list3))
