import os
import random
import sys

# make a list of words
words = [
	'apple',
	'bananna',
	'guavah',
	'coconut',
	'orange',
	'strawberry',
	'lime',
	'grape',
	'melon',
	'lemon',
	]

def clear():
	if os.system == 'nt':
		os.system('cls')
	else:
		os.system('clear')

# draw guessed letters, spaces and strikes
def draw(bad_guesses, good_guesses, secret_word):
	clear()
	
	print('strikes: {}/7'.format(len(bad_guesses)))
	print('')
	
	for letter in bad_guesses:
		print(letter, end='')
	print('\n\n')
	
	for letter in secret_word:
		if letter in good_guesses:
			print(letter, end='')
		else:
			print('_', end='')
				
	print('')
	
def get_guess(bad_guesses, good_guesses):
	while True:
		# take guess
		guess = input("Guess a letter: ").lower()
			
		if len(guess) != 1:
			print("you can only guess a single letter")
			continue
				
		elif guess in bad_guesses or guess in good_guesses:
			print("you've already guessed that before")
			continue
			
		elif not guess.isalpha():
			print("you can only guess letters")
			continue	
	
		else:
			return guess
	
def play(done):	
	# pick a random word
	secret_word = random.choice(words)
	good_guesses = []
	bad_guesses = []
	
	while True:
		draw(bad_guesses, good_guesses, secret_word)
		guess = get_guess(bad_guesses, good_guesses)
		
		if guess in secret_word:
			good_guesses.append(guess)
			found = True
			for letter in secret_word:
				if letter not in good_guesses:
					found = False
			if found:
				print("You win!")
				print("The secret word was {}".format(secret_word))
				done = True
		else:
			bad_guesses.append(guess)
			if len(bad_guesses) == 7:
				draw(bad_guesses, good_guesses, secret_word)
				print("You lost!")
				print("The secret word was {}".format(secret_word))
				done = True
		
		if done:
			play_again = input("play again? y/n ")
			if play_again.lower() != 'n':
				return play(done=False)
			else:
				sys.exit()
				

def welcome():
	start = input("Press enter/return to start or Q to quit: ").lower()
	if start == 'q':
		print("Bye!")
	else:
		return True
	


	

#while True:
#	start = input("Press enter/return to start, or Q to quit: ")
#	if start.lower() == 'q':
#		break
#		
#
#	
#	# draw spaces
#	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
#		
#		if guess in secret_word:
#			good_guesses.append(guess)
#			if len(good_guesses) == len(list(secret_word)):
#				print("You win! The word was {}".format(secret_word))
#				break
#		else:
#			bad_guesses.append(guess)
#			
#	# print win/lose
#	else:
#		print("You didnt get it the word was {}".format(secret_word))

		
'''
New terms

and - lets us define two conditions that must be True

or - lets us define two conditions, one of which must be True

str.isalpha() - Returns whether or not all of the characters in a string are alphabetical
Did you notice?

There's a tricky condition (on purpose) in the final version of our code from this video. Words that have repeated characters won't be marked as correct once they're all correctly guessed due to our len() comparisons. See if you can find a way to fix that yourself!

We'll write a version without that bug in the next video.
'''

# Using the os and sys libraries give us a lot more power outside and inside of Python. 
