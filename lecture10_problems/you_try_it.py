############### YOU TRY IT #######################
# Write a function that meets the specification:
def make_ordered_list(n):
    """n is a positive int
    Returns a list containing all ints in order
    from 0 to n (inclusive)
    """
    # your code here

    counter = 0
    list_of_nums = []
    while counter <= n:
        list_of_nums.append(counter)
        counter += 1
    return list_of_nums


print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6]

#####################################################


############ YOU TRY IT ###############
def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elements equal to e.
    """
    # your code here
    new_list = []
    for item in L:
        if item != e:
            new_list.append(item)

    return new_list


# L = [1,2,2,2]
# print(remove_elem(L, 2))    # prints [1]
# L = [1,2,2,2]
# print(remove_elem(L, 1))    # prints [2,2,2]
L = [1, 2, 2, 2]
print(remove_elem(L, 0))  # prints [1,2,2,2]


#######################################
####### YOU TRY IT ###################
# Write a function that meets this specification
def count_words(sen):
    """sen is a string representing a sentence
    Returns how many words are in sen (i.e. a word is a
    a sequence of characters between spaces."""
    # your code here
    return len(sen.split(" "))


# s = "Hello it's me"
# print(count_words(s))   # prints 3

# s = "I just took a DNA test turns out I'm 100% splitting strings"
# print(count_words(s))   # prints 12

###########################################
