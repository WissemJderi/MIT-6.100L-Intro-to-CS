s = "abca"
unique_char = ""

for char in s:
    print(char)
    if char not in unique_char:
        unique_char += char
        
print(f"Unique chars: {len(unique_char)}")