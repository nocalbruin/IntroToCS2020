import random
import time
#
#
def get_word():
	secret_words = ["apples","bananas","rice","bread","monkey","snake"]
	return random.choice(secret_words)

word = get_word()
length = len(word)
count = 0
display = '*' * length

def hangman(count, display, word):
	limit = 3
	guess = input("The secret word has "+display+" letters. Enter your guess: ")
	if guess in word:
		index = word.find(guess)
		word = word[:index] + "*" + word[index+1]
		display = display[:index] + guess + display[index + 1]
	else:
		count += 1
		if count == 1:
			print ("Wrong letter. 2 tries left.")
			
hangman(count,display,word)
			
		
	
