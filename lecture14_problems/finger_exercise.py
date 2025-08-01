def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    # Your code here
    new_list = []
    for i in aDict:
        if aDict[i] == target:
            new_list.append(i)
    return sorted(new_list)


# Examples:
aDict = {1: 2, 2: 4, 5: 2}
target = 2
# print(keys_with_value(aDict, target))  # prints the list [1,5]

############################################################


def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a
    positive value.
    """
    # Your code here
    sorted_list = []
    for i in d:
        total = 0
        for j in d[i]:
            total += j
        if total >= 0:
            sorted_list.append(i)
    return sorted(sorted_list)


# Examples:
d = {5: [2, -4], 2: [1, 2, 3], 1: [2]}
print(all_positive(d))  # prints the list [1, 2]
