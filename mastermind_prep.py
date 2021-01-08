# Mastermind!

import random


def greet_instruct():
    """greets the user and displays instructions based on prior knowledge""" 

    print("Welcome to Mastermind!")
    print()
    print("Do you know how to play?")
    knowledge = input("Y/N > ").upper()

    if knowledge == "N" or knowledge == "NO":
        print("The Computer will create a secret code (with digits that can be repeated) based on the difficulty level you select.")
        print()
        print("Easy: a 4-digit code with digits from the range 2-7, inclusive.") 
        print()
        print("Medium: a 5-digit code with digits from the range 2-7, inclusive.")
        print()
        print("Hard: a 5-digit code with digits from the range 2-9, inclusive.")
        print()
        print("Your goal is to guess the secret code in 10 tries or fewer!")
        print()
        print("When you make a guess, you will get feedback telling you how many digits are correct AND in the correct place (shown by a '1'), how many digits are correct BUT NOT in the right place ('0') and how many digits in your guess are not in the secret code at all ('-'). This feedback will be displayed in no particluar order.")
        print()
        print("For example if the secret code is 7734, and you guess 3624, you will get the following feeback:")
        print()
        print("Your Guess       Feedback")
        print("3624             -10-")
        print()
        print("This shows that one of the digits is correct and in the correct space (the '4'), one of the digits is correct BUT NOT in the correct place (the '3') and two of the digits do not appear in the secret code at all (the '7' and '7')")
        print()
        print("The game ends when you guess the secret code correctly or run out of tries (10)!")
        print()


    if knowledge == "Y" or knowledge == "YES":
        print("Awesome! Just FYI, in this version, digits can be repeated in the code, you have 10 attempts to guess the secret code, and there are three levels to choose from:")
        print("Easy: a 4-digit code with digits from the range 2-7, inclusive.") 
        print()
        print("Medium: a 5-digit code with digits from the range 2-7, inclusive.")
        print()
        print("Hard: a 5-digit code with digits from the range 2-9, inclusive.")
        print()


def get_level():
    """returns a tuple that will be used to store values based on difficulty chosen"""

    print("Which level would you like to play: easy, medium or hard?")
    level = input("> ").lower()

    if level == "easy" or level == "e":
        #level_tuple = (code length, min digit, max digit)
        easy_level = (4, 2, 7)

        return easy_level

    elif level == "medium" or level == "m" or "med" in level:
        med_level = (5, 2, 7)

        return med_level

    elif level == "hard" or level == "h":
        hard_level = (5, 2, 9)
    
        return hard_level


def generate_code(level):
    """returns a string of given code_length from random numbers in range min_digit to range max_digit, inclusive from a tuple argument being passed in"""
    #level_tuple = (code length, min digit, max digit)
    digits = []
    inclusive_range = level[2] + 1
    for i in range(level[0]):
        digits.append(random.randrange(level[1], inclusive_range))
        
    digits_strings = [str(digit) for digit in digits]
    secret_code_str = "".join(digits_strings)
        

    return(secret_code_str)


def initialize_game(level):
    """Gives instructions based on level chosen and returns a list with one item that will act as a template for feedback to be added to"""

    # Creating a list to append feedback to from all previous turns and display
    results = ["Your Guess   Feedback      1 == correct, 0 == partial correct, - == wrong"]

    print()
    print(f"Let's get started! Keep in mind: the code is {level[0]} digits long including ONLY numbers from {level[1]}-{level[2]}, inclusive (digits can be repeated).")
    print()
    print("'1' == correct digit in correct place.'0' == correct digit in wrong place. '-' == digit is incorrect.")
    print()
    return results


def check_no_turns_left(turns, code):
    """Checks to see if player has run out of turns (10) and returns True if they have"""

    if turns > 9:
        print()
        print("Oh no! You ran out of turns! Game Over.")
        print(f"The correct code was {code}. So close!")            
        print()
        return True


def get_valid_player_guess(level):
    """Gets input guess from user, ensures that it is a valid length for the level chosen, and returns a valid guess"""

    print("Guess the code!")
    print()
    guess = input(" > ")
    print()

    while (len(guess) != level[0]):
        print(f"Sorry, that's invalid. The length of the code must be {level[0]} digits long.")
        print("Try guessing again!")
        print()
        guess = input("> ")
        print()
        
    return guess


def check_win(guess, code):
    """Checks if player has won and returns True if they have"""

    if guess == code:
        print("Congratulations! You won! Woo Hoo!")
        print()
        return True


def generate_feedback(code, level, guess, results):
    """Checks the player's guess against the secret code and prints a list with all of their guesses along with feedback about them"""

    # Creating a list that will update each time a code is entered
    feedback = []
    # Creating lists of the code and user's guess to remove from when I find a match so that numbers don't get counted in feedback twice as full match and as partial match
    temp_code = list(code)
    temp_guess = list(guess)
    # Counter for how many items have been removed from the above lists to keep index in sync
    pops_for_match = 0

    for i in range(level[0]):
        if guess[i] == code[i]:
            feedback.append("1")
            temp_code.pop(i - pops_for_match)
            temp_guess.pop(i - pops_for_match)
            pops_for_match += 1


    for i in range(len(temp_guess)):
        if temp_guess[i] in temp_code:
            feedback.append("0")
            temp_code.remove(temp_guess[i])
    

        elif temp_guess[i] not in temp_code:                feedback.append("-")

    # Randomize/reorder the feedback of 0s and 1s displayed
    randomized_feedback = random.sample(feedback, len(feedback))
    results.append(f"{guess}          " + ''.join(randomized_feedback))

    for result in results:
        print(result) 

    print()
    

def count_turns(turns):
    """Keeps track of and returns player turns taken and prints turns they have left"""

    turns += 1
    turns_left = (10 - turns)
    if turns_left > 0:
        print(f"You have {turns_left} turn(s) left.")
        print()

    return turns


def play_a_round():
    """Calls all functions needed to play one round of Mastermind"""

    given_level = get_level()

    secret_code_str = generate_code(given_level)
    
    turns_taken = 0
    
    result_board = initialize_game(given_level)

    # print(secret_code_str)

    while True:

        if check_no_turns_left(turns_taken, secret_code_str) == True:
            break
    
        player_guess = get_valid_player_guess(given_level)

        if check_win(player_guess, secret_code_str) == True:
            break

        generate_feedback(secret_code_str, given_level, player_guess, result_board)

        turns_taken = count_turns(turns_taken)


def play_again():
    """Asks player if they want to play again and returns True if they do and False if they don't"""

    print("Do you want to play again? Y/N")
    again = input("> ").upper()
    print()

    if again == "Y" or again == "YES":
        return True

    else:
        print()
        print("Goodbye!")
        return False


def play_game():
    """Runs the full game with multiple rounds until player says no"""

    greet_instruct()

    while True:

        play_a_round()
   
        if play_again() == False:
            break

play_game()