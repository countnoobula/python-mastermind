from random import randint # We are telling it to import the randint function from the random package so we can use it to generate a secret code :)

numberOfTries = 20;
attemptedTries = 0;
secretCode = 0;

def printWelcome(): # Keep in mind the : at the end of the line
	# The indentation is also really important. It separates code blocks for the interpreter.
	print("Welcome to Code Breaker!");
	print("");
	print("The instructions are simple:");
	print(" - A secret 4 digit number will be generated between 1000 and 9999.");
	print(" - You will be asked for a 4 digit number.");
	print(" - You will be told how many numbers from your input are in the correct place");
	print(" - When you get them all right. You have won!");
	print(" - You only have " +  str(numberOfTries) + " attempts to guess it correctly."); # You can't join words(strings) and numbers (integers). So str() turns the integer into a string
	print(" - You can type 'q' to quit the game while playing.")

def askReady():
	answer = raw_input("Are you ready? [yes|no]");

	if answer.lower().startswith('y'):
		print("Let's begin");
	else:
		print("Come back when you are");
		exit();

def generateSecretCode():
	# We use global because the variables are outside of the function.
	# It is unsafe in big projects, but for small scripts is a really easy way to do it.
	global secretCode;

	secretCode = str(randint(1000, 9999));
	# print("The secret number is: " + secretCode); # Remove the # to see what the secret number is when you play the game.

def endGame():
	global secretCode;
	global numberOfTries;

	print("");
	print("You cracked the code!")
	print("The secret code was: " + secretCode);
	print("There were " + str(numberOfTries - attemptedTries) + " tries left to guess it.");
	print("Thank you for playing.");
	exit();

def askGuess():
	global numberOfTries;
	global attemptedTries;
	global secretCode;

	while (True):
		guess = raw_input("You have " + str(numberOfTries - attemptedTries) + " guesses left. What is your guess? ");

		if (len(guess) == 4):
			numberOfCorrect = 0;

			for index, digit in enumerate(guess): # Enumerate with the special for loop allows us to get the position of the digit in the guess, and what it is. 
				if (digit == secretCode[index]): # This checks that the position [index] of the number in this entry, is the same as the other.
					numberOfCorrect += 1; # This marks that you got a correct number

			print("You have " + str(numberOfCorrect) + " numbers correct in their position.");

			if (numberOfCorrect == 4):
				endGame();

			attemptedTries =+ 1;
		else:
			if (guess[0] == 'q'):
				print("Quitting game...");
				exit();

			print("Please input a 4 digit number.");

# Functions must be called after they are declared, because otherwise they don't exist.
# Function hoisting does not exist in all languages, python is not one of those
printWelcome();
askReady();
generateSecretCode();
askGuess();1
