############### YOU TRY IT #####################
# Write a function that meets these specifications:
def char_counts(s):
    """s is a string of lowercase chars
    Returns a tuple where the first value is the
    number of vowels in s and the second value
    is the number of consonants in s
    """
    # your code here
    vowels = "aeiou"
    vowels_counter = 0
    consonants_counter = 0
    for char in s:
        if char in vowels:
            vowels_counter += 1
        else:
            consonants_counter += 1
    return (vowels_counter, consonants_counter)


print(char_counts("abcd"))  # prints (1,3)
print(char_counts("zcght"))  # prints (0,5)

##################################################
