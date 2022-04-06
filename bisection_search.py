cube = 100
epsilon = 0.1
num_guesses = 0

low = 0
high = cube
guess = (high+low)/2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0
    num_guesses += 1

print(f"{guess} is the close cube root of {cube}, guess: {num_guesses}")    
epsilon = 0.1
num_guesses = 0

low = 0
high = cube
guess = (high+low)/2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0
    num_guesses += 1

print(f"{guess} is the close cube root of {cube}, guess: {num_guesses}")    