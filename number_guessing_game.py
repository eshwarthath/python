import random
print("Welcome to the Number Guessing Game!")
def play_game():
    random_number = random.randint(1, 100)


    print("I'm thinking of a number between 1 and 100.")


    choice_for_game = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if choice_for_game == 'easy':
         attempts = 10
         score = 100
    if choice_for_game == 'hard':
         attempts = 5
         score = 50

    while attempts > 0:
       print(f"You have {attempts} attempts remaining to guess the number.")
       print(f"your current score is {score}.")
       guess = int(input("Make a guess: "))

       if guess == random_number:
           print(f"You got it! The answer was {random_number}.")
           if choice_for_game == 'easy':
                print(f"You guessed the number in {10 - attempts} tries.")
           else:
                print(f"You guessed the number in {5 - attempts} tries.")
           print(f"your final score is {score}.")
           play_again = input("do you want to play again? (yes or no):")
           if play_again == 'yes':
               print("\n" * 20)
               play_game()
           else:
               print("Thanks for playing!")
           break
       elif guess > random_number:
           print("Too high.")
       else:
           print("Too low.")

       score -= 10
       attempts -= 1

       if attempts > 0:
           print("Guess again.")
       else:
           print("You've run out of guesses.")
           print(f"The number was {random_number}. sorry you have lost the game.")
           play_again = (input("do you want to play again? (yes or no):"))
           if play_again == 'yes':
               print("\n" * 20 )
               play_game()
           else:
               print("Thanks for playing!")
               break
play_game()





