import random

# A list of words that 
potential_words = ["silent","fox","jump","coding","python","float","length","print","fruit"]

word = random.choice(potential_words)

# Use to test your code:


# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_"]*len(word) #TIP: the number of letters should match the word


# Some useful variables
guesses = [15]
maxfails = 10
fails = 0

while fails < maxfails:
        guess = input("Guess a letter: ").lower()
        if guess in word:
                 print("You have guessed the correct letter! Congrats:)")
                 index = word.index(guess)
                 current_word[index]=guess
                 print(current_word)
                 if "_" not in current_word:
                     break
        else:
                 print(" incorrect, try again.")
                 fails = fails+1
                 print("You have " + str(maxfails - fails) + " tries left!")
                 if fails==maxfails:
                     print("You lose. Better luck next time!")
print(word)

