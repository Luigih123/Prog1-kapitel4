import random

number = random.randint(1, 100_000_000)
guesses = 0
guess = 0

while guess != number:
    guesses += 1
    guess = int(input("Gissa på ett heltal mellan 1 och 100_000_000: "))

    if guess < number:
        print(f"Din gissning {guess} är för liten.")
    elif guess > number:
        print(f"Din gissning {guess} är för stor.")
    
print(f"Grattis du behövde {guesses} gissningar!")