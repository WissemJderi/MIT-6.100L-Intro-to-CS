############ YOU TRY IT ###############
# This one is similar to remove_elem from lec10 except that remove_elem
# returns a new list and this one mutates the parameter L (and returns None)
def remove_all(L, e):
    """
    L is a list
    Mutates L to remove all elements in L that are equal to e
    Returns None.
    """
    # your code here
    L_copy = L[:]
    L.clear()
    for i in L_copy:
        if i != e:
            L.append(i)


# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)    # prints [1]

# Lin = [1,2,2,2]
# remove_all(Lin, 1)
# print(Lin)    # prints [2, 2, 2]

Lin = [1, 2, 2, 2]
remove_all(Lin, 0)
print(Lin)  # prints [1, 2, 2, 2]

#######################################
