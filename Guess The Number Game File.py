#RAMDOM PLAY version 1.1
import random
import pyfiglet

global myName

def easy():
	number = random.randint(1, 20)
	print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
	print('you have 5 guesses.')
	print(input("Please Enter to continue.."))
	guessesTaken = 0

	while guessesTaken < 6:
		print('Take a guess.')
		guess = input()
		guess = int(guess)
		guessesTaken = guessesTaken + 1
		if guess < number:
			print('Your guess is too low.') 
		if guess > number:
			print('Your guess is too high.')
		if guess == number:
			break
			
	if guess == number:
		guessesTaken = str(guessesTaken)
		print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
	if guess != number:
		number = str(number)
		print('Nope. The number I was thinking of was ' + number)

def medium():
	number = random.randint(1, 30)
	print('Well, ' + myName + ', I am thinking of a number between 1 and 30.')
	print('you have 7 guesses.')
	print(input("Please Enter to continue.."))
	guessesTaken = 0
	while guessesTaken < 8:
		print('Take a guess.')
		guess = input()
		guess = int(guess)
		guessesTaken = guessesTaken + 1
		if guess < number:
			print('Your guess is too low.') 
		if guess > number:
			print('Your guess is too high.')
		if guess == number:
			break

	if guess == number:
		guessesTaken = str(guessesTaken)
		print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
	if guess != number:
		number = str(number)
		print('Nope. The number I was thinking of was ' + number)

def hard():
	number = random.randint(1, 50)
	print('Well, ' + myName + ', I am thinking of a number between 1 and 50.')
	print('you have 10 guesses.')
	print(input("Please Enter to continue.."))
	guessesTaken = 0
	while guessesTaken < 11:
		print('Take a guess.')
		guess = input()
		guess = int(guess)
		guessesTaken = guessesTaken + 1
		if guess < number:
			print('Your guess is too low.') 
		if guess > number:
			print('Your guess is too high.')
		if guess == number:
			break

	if guess == number:
		guessesTaken = str(guessesTaken)
		print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
	if guess != number:
		number = str(number)
		print('Nope. The number I was thinking of was ' + number)
		print(+ myName +'Better Luck Next Time.')
def extremehard():
	number = random.randint(1,100)
	print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
	print('you have 15 guesses.')
	print(input("Please Enter to continue.."))
	guessesTaken = 0
	while guessesTaken < 16:
		print('Take a guess.')
		guess = input()
		guess = int(guess)
		guessesTaken = guessesTaken + 1
		if guess < number:
			print('Your guess is too low.') 
		if guess > number:
			print('Your guess is too high.')
		if guess == number:
			break

	if guess == number:
		guessesTaken = str(guessesTaken)
		print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
	if guess != number:
		number = str(number)
		print('Nope. The number I was thinking of was ' + number)
		print(+ myName +'Better Luck Next Time.')

art = pyfiglet.figlet_format("GUESS THE NUMBER GAME") 
print(art) 
print('Hello! What is your name?')

myName = input()
print('Hi '  + myName + '   Welcome To Our Game\n''Before we start,Please select your Level.\n')
print("1.EASY\n2.MEDIUM\n3.HARD\n4.EXTREME HARD")

user_input=int(input())
easy_play =(1)
medium_play =(2)
hard_play =(3)
extreme_play=(4)

if user_input == easy_play:
	easy()
if user_input == medium_play:
	medium()
if user_input == hard_play:
	hard()
if user_input ==extreme_play:
	extremehard()