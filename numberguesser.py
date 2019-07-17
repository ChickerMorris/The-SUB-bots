#number gueeser
#Author Zachary Morris

import random
import time

print("Welcome to number guesser.")

min = int(input("What is the lowest value?"))
max = int(input("What is the highest value?"))

count = 0
while True:
	number = random.randint(min, max)
	guess = int(input("guess a number?"))
	time.sleep(3)
	if guess == number:
		print("Yay you won!")
		break
	elif guess > number:
		print("You won, just kidding, you should have found a better way to waste your time until you eventually die.")
		count += 1
	elif guess < number:
		print("Too low in the ground to understand which numbr it is.")
		count += 1
	elif count == 3:
		print("You lost")
	else:
		print("you broke it! :(")
		count += 1
