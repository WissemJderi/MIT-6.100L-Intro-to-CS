n = 254
num_of_guesses = 0
high = 1000
low = 0
guess = int((high + low) / 2)
while guess != n:
    if guess > n:
        high = guess - 1
    else:
        low = guess + 1
    guess = int((high + low) / 2)
print(guess)
