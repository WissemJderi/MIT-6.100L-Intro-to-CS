########################################################################
# Problem 1: List concatenation
original_list = [1,2,35,10,5,8,9,23]

# a) Using List concatenation create a new list from the orignal list, 
# removing all multiples of 5 from a list of numbers.
# expected output: [1, 2, 8, 9, 23]
# INSERT CODE HERE
not_multiple_of_five = [num for num in original_list if num % 5 != 0]
# print(not_multiple_of_five)
# b) Using list concatenation create a new list from the original list, 
# where each element is half the original element
# Expected output: [0.5, 1.0, 17.5, 5.0, 2.5, 4.0, 4.5, 11.5]
# INSERT CODE HERE
half_the_original = [num / 2 for num in original_list ]
# print(half_the_original)
########################################################################
# Problem 2: Write a Function to insert a specified element x in a given list 
# after every nth element.
# Return the new list. 
# Example
# Original list:
# [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in list after every 4th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

def insert_element_list1(lst, x, n):
    """
    Parameters:
    lst: input list
    x: element to insert
    n: x will be inserted after every nth element
    Returns: new modified list 
    """
    # INSERT CODE HERE
    new_list = lst[:]
    # Add this to know where is the fourth item when the list grows
    counter = 0
    for i in range(len(new_list)):
        if (i) > 1 and i  % n == 0:
            lst.insert(i + counter, x)
            counter += 1

    return lst

# testing
nums = [1, 3, 5, 7, 9, 11,0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
x = 20
n = 4
# print(insert_element_list1(nums, x, n))


########################################################################
# Problem 3: Write a Function to sort list of lists containing integers such that the 
# sub-lists are sorted in increasing order. How would you sort in decreasing order?

# Example:
# Original list of tuples:
# [[10, 10.12, 10.11], [5, 5.3, 4.9], [2.4, 2.6, 2.2]]
# Expected output:
# [[10, 10.11, 10.12], [4.9, 5, 5.3], [2.2, 2.4, 2.6]]

def sort_list_of_lists(lst):
    """
    Parameters:
    lst: input list
    n: index to sort by
    Returns: the sorted list 
    """
    # INSERT CODE HERE
    for i in range(len(lst)):
    
        lst[i] = sorted(lst[i])
        
    
    return lst

# testing
items = [[10, 10.12, 10.11], [5, 5.3, 4.9], [2.4, 2.6, 2.2]]
# print(sort_list_of_lists(items))


########################################################################







