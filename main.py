import random

difficulty = input("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': """)
answer = random.randint(1, 100)

def guessing_game():
    global game_over
  
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
      
    game_over = False
      
    while not game_over:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
      
        if guess > answer:
            print("Too high.")
            attempts -= 1
        elif guess < answer:
            print("Too low.")
            attempts -= 1
        else:
            print("Correct!")
            break
          
        if attempts == 0 and guess != answer:
            print("You have run out of guesses. You lose!")
            game_over = True
        elif guess != answer:
            print("Guess again.")

guessing_game()
