import random
import time 

print("\nWelcome to the GUESSING GAME! I'm goind to pick up a number between 1 and 100.\n")

time.sleep(2)
print("Thinking a number...")
time.sleep(2)

guess = int(input("Whats is your guess? "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong! You need to guess higher. Whats is your guess? "))
    else:
         guess = int(input("Wrong! You need to guess lower. Whats is your guess? "))


print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses.")