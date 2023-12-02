import random
import math

low = int(input("Enter min low value: "))
high = int(input("Enter max high value: "))


x = random.randint(low, high)
max_attempts = round(math.log(high - low + 1, 2))
print("\n\tYou've only ", max_attempts, " chances to guess the integer!\n")

count = 0

while count < max_attempts:
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulation you did it in ", count, " try")
        break

    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")


if count >= max_attempts:
    print(f"\nThe number is {x}")
    print("\tBetter luck next time")

