my_str = "python is great"
new_str = ""

for i in range(len(my_str)):
    if i % 2 != 0:

        new_str += my_str[i]
print(new_str)
