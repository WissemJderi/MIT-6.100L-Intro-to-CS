n = 27
found = False

for i in range(0, n + 1):
    if (i ** 3) == n:
        print(i)
        found = True

if not found: 
    print("error")

