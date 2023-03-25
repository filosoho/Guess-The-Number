#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game! 🤓")
print("\nI'm thinking of a number between 1 and 100.\n")

number = random.randint(1, 100)


def play(level):
  if level == 'easy':
    attempts = 10
  elif level == 'hard':
    attempts = 5

  while attempts != 0:
    #print("-------------------------------------------------------------")
    print(f"You have {attempts} attempts remaining to guess the number.")
    print("-------------------------------------------------------------")

    while True:
      try:
        guess = int(input("Make a guess: "))
        break
      except ValueError:
        print("==========================================")
        print("Incorrect input. Please enter a number. 🙄")
        print("==========================================")

    attempts -= 1
    if attempts == 0:
      print("-------------------------------------------------------------")
      print("You've run out of guesses, you lose. 😤")
      print("-------------------------------------------------------------")
    elif guess == number:
      print(f'''
                                      _______
                                     |       |
                                    (| 🏆🥇  |)
                                     |  #1   |
                                      \     /
                                       `---'
                                       _|_|_
          🏆🥇  (҂◡̀_◡́)ᕤ  🎯💯                    
                                                
   You got it! The answer was {number}. 😁🎉                                               
   ''')
      print("-------------------------------------------------------------")
      attempts = 0
    elif guess > number:
      print("\nToo high.\nTry again. 🤨")
      print("-------------------------------------------------------------")
    elif guess < number:
      print("\nToo low.\nTry again. 🤔")
      print("-------------------------------------------------------------")

while True:
  print("-------------------------------------------------------------")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  print("\n")

  if level == 'hard' or level == 'easy':  
    play(level)
    break
  else:
    print("==============================")
    print("Incorrect input. Try again. 🙄")
    print("==============================") 