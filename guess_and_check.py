cube = 100
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and num_guesses <= cube:
    guess += increment
    num_guesses += 1

if ((guess**3) - cube) >= epsilon:
    print(f"{guess} is the close cube root of {cube}, guess: {num_guesses}")    
else:
    print(f"Failed {guess} is not the root of {cube}, guess: {num_guesses}")
    
    