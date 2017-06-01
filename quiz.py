# IPND Code your own quiz assignment

#blanks array to use as answer placeholders
blanks = ["___1___", "___2___", "___3___", "___4___"]

# three levels to pass to play_game function.
easy_paragraph = '''An ___1___, is not just any set of instructions. They have to be precise and unambiguous enough to be executed by a computer. 
Believe it or not, every algorithm, no matter how complex, can be reduced to just these three operations: and, or, and ___2___. 
Every algorithm has an ___3___ and an ___4___, the data goes into the computer, the algorithm does what it will with it, and out comes the result. 
The Master Algorithm, Reference''' 
medium_paragraph = '''Every algorithm has an ___1___ and an ___2___: the data goes into the computer, the ___3___ does what it will with it, 
and out comes the result. Machine ___4___ turns this around: in goes the data and the desired result and out comes the algorithm that turns one 
into the other. The Master Algorithm, Reference''' 
hard_paragraph = '''We can think of ___1___ learning as the ___2___ of programming, in the same way that the ___3___ root is the inverse of the square, 
or ___4___ is the inverse of differentiation. The Master Algorithm, Reference'''

# replacement words/answers at three levels to be passed in to the play game function. 
easy_answers = ["algorithm", "not", "input", "output"]
medium_answers = ["input", "output", "algorithm ", "learning"]
hard_answers = ["machine", "inverse", "square", "integration"]	

player = ""

#Functions

def greeting(player):
	#request user name, welcome him/her to the game, direct them to enter one of three choices
	player = raw_input("What is your name? ")
	print "\n Welcome, " + player + " to the Fill in the blanks game!"
	print "\n Please enter a level (easy|medium|hard) to start the game"

def process_level(level):
	#based on level selected, the level will be indicated to screen and level will be set for game play
	if level == "easy":
		print "\n You have chosen the easy level\n"
		return easy_paragraph, easy_answers

	elif level == "medium":
		print "\nYou have chosen the medium level\n"
		return medium_paragraph, medium_answers

	else: # For level 3.
		print "\nYou have chosen the hard level\n"
		return hard_paragraph, hard_answers

def word_in_blanks(word, blanks):
	# This function Returns 'word' if that matches up with the current word in the paragraph.
	for blank in blanks: # For every blank in the blanks array.
		if blank in word: # If blank is in answer.
			return blank  # returns blank
	return None

def replace_the_blank(word, replaced, blanks, user_answer, index): 
	"""To replace each blank with its correct answer. Part 2.
	Inputs: 'blanks' list, the replaced paragraph that has the correct answers so far, if applicable,
	the 'user_answer' for that blank, the index number of that 'user_answer' to correctly match that with the right blank to fill in. 
	Outputs: The correctly replaced paragraph."""

	if word_in_blanks(word, blanks) == None:
		if word not in replaced:
			replaced.append(word)
	else:
		replacement = word_in_blanks(word, blanks)
		word = word.replace(replacement, user_answer.upper())

		if replacement == blanks[index]:
			if replacement not in replaced:
				replaced.append(word)
			else:
				position = replaced.index(replacement)
				replaced[position] = word
		else:
			replaced.append(replacement)

	return replaced


def fill_in_answers(paragraph, blanks, replaced, user_answer, index): 
	#Fill each blank with an answer

	split_paragraph = paragraph.split()

	if type(replaced) == str:
		replaced = replaced.split()		

	for word in split_paragraph:
		replace_the_blank(word, replaced, blanks, user_answer, index)
		
	replaced = " ".join(replaced)
	head, sep, tail = replaced.partition("Reference") # chomps the blanks that tacked on to the end of every paragraph. 
	replaced = head + sep
	return replaced


def collect_player_answers(level, paragraph, answers):
	#collect playeranswers
	
	replaced = []

	user_answer = ""

	index = 0
	for blank in blanks:
		# questions and answers gets stated.

		question = "\nWhat is your answer for " + blank + "?"
		print question

		user_answer = raw_input("Type here: ")
		user_answer = user_answer.lower()

		while user_answer != answers[index]:
			print "\nYour answer was wrong. Please try again.\n"
			user_answer = raw_input("Type it again: ")
			user_answer = user_answer.lower()

		print "\nAwesome, " + player + ", that's correct!\n"	
									
		replaced = fill_in_answers(paragraph, blanks, replaced, user_answer, index)
		print replaced			

		index += 1
	
	return replaced, index

#Start of game

def play_game():

	greeting(player)

	level = raw_input("\n")

	if level == "easy" or level == "medium" or level == "hard":
		paragraph, answers = process_level(level)     
		print paragraph 

		replaced = collect_player_answers(level, paragraph, answers)

		print "\n " + player + ", Congratulations! You have won!\n"	
	
	else:		
		print "\n "+ player + "!,  Please type a level. Game will then start.\n"
		play_game()

play_game() 