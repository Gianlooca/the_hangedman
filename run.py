import random
import string
from constants import *


def get_acceptable_word(TEXT):
    """
    This function "get an acceptable word" from the constant TEXT and returns
     it. Then the function is called into the main() function
    """

    # This eliminates all punctuation. On the first line we create a
    # translation table which transforms all punctuation characters
    # to None, in the second line we have the translate() method which
    # actually removes all the punctuation from the TEXT constant, and
    # assigns the result to a text variable

    translation_table = str.maketrans("", "", string.punctuation)
    text = TEXT.translate(translation_table)

    # This transformes the text into a list of words

    first_list = text.split()

    # This list comprehension removes the duplicates from our original
    # list and the words words smaller than 4 characters, then transform
    # the remaining ones in uppercase

    final_list = [
        i.upper() for n, i in enumerate(first_list)
        if i not in first_list[:n] and len(i) >= 4
    ]

    # This chooses and returns a random word from the list of words

    word_in_game = random.choice(final_list)
    return word_in_game


def menu():
    """
    This function displays the main menu; the user can choose whether
    to start the game or to read the instructions on how to play.
    Since the function consists mainly of a while loop, it will continue
    running until the user starts a new game. The valid inputs are only
    's/S' to start and 'i/I' for the instructions. The function is called
    inside the main() function.
    """

    # ASCII art for the menu

    print(menu_ascii)
    while True:
        user_input = input(
            "Press S and ENTER to start a new game\n"
            "Press I and ENTER for instructions.\n"
        ).upper()
        print(end="\n")

        # If the user enters "s/S" starts a new game; if "i/I", instructions
        # are displayed; any other character will print the "else" message

        if user_input == "S":
            return True
        elif user_input == "I":
            print(
                f"""
INSTRUCTIONS:

1. You'll have to guess a random word letter by letter.
2. To guess, type a letter (A LETTER) and press enter.
3. If you guess correctly, the letter will be revealed in its exact position in
   the secret dashed word.
4. If you guess incorrectly, you will lose a life and the poor Hangman will
   start to appear.
5. The word that you have to guess can be everything: a singular name, a plural
   name, a verb, a past participle, etc.
6. You have 6 attempts to guess the correct word: head, torso, two arms and two
   legs.
   
After that, you'll become an executioner!

"""
            )
            input("Press ENTER to go back to the menu\n")
        else:
            print(
                "Remember: S to start a new game, I for instruction."
                " Please try again!\n")


def ask_user_name():
    """
    This function asks the user to input his/her name. It doesn't accept
    punctuation, spaces, numbers: just alphabetic letters. Then returns a
    username variable. The function is called inside the main() function
    """
    while True:
        username = input("Enter your name: \n")
        if username.isalpha() and not any(char.isspace() for char in username):
            return username
        else:
            print(
                f"""
This is not a concentration camp: no numbers or spaces allowed.
Enter your name again.\n"""
            )


def update_guessed_letters(letter, guessed_letters):
    """
    This function updates the list of letters already used with the new
    guessed letter and displays an "invalid" input message: one if the user
    tries to enter a character which is not alphabetical, and another one if
    an already guessed letter is entered
    """

    invalid_input_message = (
        "Ehy, you can only guess LETTERS; one at a time, though."
        " Try again."
    )

    # This if statement verifies if the letter is not alphabetic or is longer
    # than a character. In the input is invalid, the return keyword exits the
    # function

    if not letter.isalpha() or len(letter) != 1:
        print(invalid_input_message)
        return False

    # Check if the letter has already been used and in that case prints a
    # message. Otherwise, the new guessed letter is appended to the
    # guessed_letters list and displayed in the terminal

    if letter in guessed_letters:
        print("You've already used that letter.")
        return False
    else:
        guessed_letters.append(letter)
        return True


def end_game(game_over, word_in_display, word_in_game, username):
    """
    This function manages the end of the game in its two possibilities
    (play again or exit the game);
    it also prints a message in case of invalid input from the user
    """

    # If the condition of game_over is True, in both cases of victory or
    # defeat, it prints two different messages

    if game_over:
        if word_in_display == word_in_game:
            print(
                f"""
Congratulations, {username}! you guessed the word and saved an innocent
life!
"""
            )
        else:
            print(
                f"""
I have bad news, {username}: you miserably lost the game and killed a man.
In any case, the word was: {word_in_game}
"""
            )

    # While loop that keeps asking the user to enter a valid input in order
    # to start another game or exit. Any other input will cause a customized
    #  "invalid input" message

    while True:
        play_again = input(
            "Do you want to play again?\nPlease enter 'y' and ENTER "
            "for yes or 'n' and ENTER for no.\n").lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            print(f"\n{username}, thanks for playing!")
            print(TITLE)
            return False
        else:
            print("\nSeriously? Invalid input.\n")


def main():
    """
    This function handles the whole game (game settings, number of GUESSES -
    this variable is global, not local to the function scope -, etc.); it
    prints the TITLE, it runs the menu() function, contains an empty list of
    letters and, the most important thing, a while loop which basically is the
    core of the game which keeps asking the user to enter a letter and,
    depending on the guess (correct or incorrect), displays the letters inside
    the secret dashed word or the ASCII art of the hanged man adding a new
    'piece' of his body for each round, until the end of the game. It uses the
    recursion to play again the game (or not) by calling the end_game()
    function within it.
    """
    global GUESSES
    # Reset GUESSES at the beginning of each game
    GUESSES = len(HANG_STAGE) - 1
    print(TITLE)
    if menu():
        word_in_game = get_acceptable_word(TEXT)
        word_in_display = "_" * len(word_in_game)
        game_over = False
        username = ask_user_name()
        print()
        print(f"Ciao, {username}: guess the hidden word and save a life!")

        # Empty list to keep track of the already guessed letters
        guessed_letters = []

        while not game_over:
            # Prints the hangman ASCII art
            print(HANG_STAGE[7 - GUESSES - 1])

            # Prints letters guessed so far
            print('Letters you guessed so far: ', guessed_letters)

            print(word_in_display)
            print()

            # This checks if the game is ended: the loop is broken and the
            #  game_over variable becomes True if GUESSES == 0 or the word
            # which is displayed is equal to the original randomly chosen word
            if GUESSES == 0 or word_in_display == word_in_game:
                game_over = True
                break

            # Calls update_guessed_letters to handle input and printing of
            #  guessed letters
            guessed_letter = input(f"{username}, guess a letter: \n").upper()
            is_valid_input = update_guessed_letters(
                guessed_letter,
                guessed_letters
            )

            # Skips the rest of the loop if the input is invalid
            if not is_valid_input:
                continue

            # In case the letter the user enters is guessed correctly, this
            # iterates through the secret word and updates the visualization
            # of the word_in_display by indexes; otherwise, a GUESS (a 'life')
            # is subtracted
            if guessed_letter in word_in_game:
                for i in range(len(word_in_game)):
                    if word_in_game[i] == guessed_letter:
                        word_in_display = word_in_display[:i] + \
                            guessed_letter + word_in_display[i + 1:]
            else:
                GUESSES -= 1

        # Print the hangman ASCII art after each guess
        print(HANG_STAGE[7 - GUESSES - 1])

        # Call end_game() to handle the end-of-game logic
        play_again = end_game(
            game_over,
            word_in_display,
            word_in_game,
            username)
        if play_again:
            main()  # Restart the game


if __name__ == "__main__":
    main()
