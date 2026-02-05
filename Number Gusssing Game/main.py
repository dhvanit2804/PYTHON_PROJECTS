import random

n = random.randint(1, 100)

attempt = 0

print("\n--- Welcome To Number Gusseing Game ---")
print("Guess The Number Between (1 TO 100) ")

while True:

    guess_num = int(input("Enter a number between (1-100): "))
    attempt += 1

    if guess_num > n:
        print("Number is High")

    elif guess_num < n:
        print("Number is low")

    else:
        print(f"The Number you guess {guess_num} and {n} is matching")
        print("Congratulation You are Win this game")
        print(f"The total attempt: {attempt}")