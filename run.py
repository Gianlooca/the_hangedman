import random
import string

# Constants

HANG_STAGE = [
    r"""
        ,_______________
       ||--------------\
       ||              |
       ||              |
       ||
       ||
       ||
       ||
       ||
       ||
       ||
       ||
       ||\
       ||\\
       || \\
       ||  \\

        """, r"""

        ,_______________
       ||--------------\
       ||              |
       ||             _|_
       ||            {°¿°}
       ||             (¨)
       ||
       ||
       ||
       ||
       ||
       ||
       ||\
       ||\\
       || \\
       ||  \\

        """, r"""

        ,_______________
       ||--------------\
       ||              |
       ||             _|_
       ||            {°¿°}
       ||           __(¨)__
       ||           |   ♂ |
       ||           |DEATH|
       ||           |_ROW_|
       ||
       ||
       ||
       ||\
       ||\\
       || \\
       ||  \\

        """, r"""

        ,_______________
       ||--------------\
       ||              |
       ||             _|_
       ||            {°¿°}
       ||           __(¨)__
       ||          /|   ♂ |
       ||         //|DEATH|
       ||        // |_ROW_|
       ||      `¡¡'
       ||
       ||
       ||\
       ||\\
       || \\
       ||  \\

        """, r"""

        ,_______________
       ||--------------\
       ||              |
       ||             _|_
       ||            {ʘ¿ʘ}
       ||           __(¨)__
       ||          /|   ♂ |\
       ||         //|DEATH|\\
       ||        // |_ROW_| \\
       ||      `¡¡'         '¡¡`
       ||
       ||
       ||\
       ||\\
       || \\
       ||  \\

        """, r"""

        ,_______________
       ||--------------\
       ||              |
       ||             _|_
       ||            {ʘ¿ʘ}
       ||           __(¨)__
       ||          /|   ♂ |\
       ||         //|DEATH|\\
       ||        // |_ROW_| \\
       ||      `¡¡' / /     '¡¡`
       ||          / /
       ||         | |
       ||\        μμμ
       ||\\
       || \\
       ||  \\

        """, r"""

        ,_______________
       ||--------------\
       ||              |
       ||             _|_
       ||            {×¿×}
       ||           __(Ü)__
       ||          /|   ♂ |\
       ||         //|DEATH|\\
       ||        // |_ROW_| \\
       ||      `¡¡' / / \ \ '¡¡`
       ||          / /   \ \
       ||         | |     | |
       ||\        μμμ     μμμ
       ||\\
       || \\
       ||  \\

        """
]

TITLE = r"""
     ____    ____        __________________     ____
    _\HHH\  _\HHH\      /GGGGGGGGGGGGGGGGG/\   /NNN/_
    \ \HHH\ \ \HHH\    /\GGGGGGGGGGGGGGGG/ /  /NNN/ /
     \ \HHH\ \/HHHH\   \ \GGG\___________\/  /NNNNNNNNN\
      \ \HHH\/H/\HHH\   \ \GGG\    /GGGGGG/ /NNN/¯¯\NNNN\
       \ \HHHH/\ \HHH\   \ \GGG\__/GG/\__/ /NNN/ /¯¯\NNNN\
        \ \HHH\ \ \HHH\__ \ \GGGGGGG/ /   /NNN/ /    \NNNN\__
         \ \HHH\ \ \HHHHHH\\ \GGGGG/ /   /NNN/ /     /NNNNNNN|_
          \____\  \_______\ \/_____\/    /____/       /________|

                          ____         ____            ____
  ... \     ___     \   \  ___\  \--.  \   \  \--.,-.   ___\  \--.
    \  \--. \__\     \---\ \   \  \  \  \___\  \  \  \  \   \  \  \
     \  \  \ \___,    \   \ \___\_ \  \, ;___\  \  \  \  \___\_ \  \

                           |¯/¯¯¯i
                           |/    i
                           |     ð <(life is but a slipknot)
                           |    /|\
                           |    / \
                           |
"""
TEXT = (f"""
"But my brain got more and more confused. At last I sprang out of bed to
look for the water-tap. I was not thirsty, but my head was in a fever, and
I felt an instinctive longing for water. When I had drunk some I got into
bed again, and determined with all my might to settle to sleep. I closed my
eyes and forced myself to keep quiet. I lay thus for some minutes without
making a movement, sweated and felt my blood jerk violently through my
veins. No, it was really too delicious the way he thought to find money in
the paper cornet! He only coughed once, too! I wonder if he is pacing up
and down there yet! Sitting on my bench? the pearly blue sea ... the
ships...."
"I opened my eyes; how could I keep them shut when I could not sleep? The
same darkness brooded over me; the same unfathomable black eternity which
my thoughts strove against and could not understand. I made the most
despairing efforts to find a word black enough to characterize this
darkness; a word so horribly black that it would darken my lips if I named
it. Lord! how dark it was! and I am carried back in thought to the sea and
the dark monsters that lay in wait for me. They would draw me to them, and
clutch me tightly and bear me away by land and sea, through dark realms
that no soul has seen. I feel myself on board, drawn through waters,
hovering in clouds, sinking--sinking."
""")

# This constant is the number of "lives" for each game.
# It is equal to the number of HANG_STAGE (which are 7) - 1, because each game
# starts already with the first "stage" (that is the ASCII art of the empty
# gallows)

GUESSES = len(HANG_STAGE) - 1


# Functions

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

    print(r"""
    ʔ^^^^^^^^^^^^^^^^^^^ʕ
    |    THE HANGMAN    |
    |  S. Start Game    |
    |  I. Instructions  |
    |___________________|
        |   |   |   |
        ð   ð   ð   ð
       /|\ /|\ /|\ /|\
       / \ / \ / \ / \
    """)
    while True:
        user_input = input(
            "Press S to start a new game\nPress I for instructions.\n"
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

5. You have 6 attempts to guess the correct word: head, torso, two arms and two
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
This is not a concentration camp: no number or spaces allowed.
Enter your name again.\n"""
            )


def update_guessed_letters(letter, guessed_letters):
    """
    This function updates the list of letters already used with the new 
    guessed letter, prints it for each round and displays two "invalid" input
    messages: one if the user tries to enter a character which is not
    alphabetical, and another one if an already guessed letter is entered
    """

    invalid_input_message = (
    "Ehy, you can only guess LETTERS; one at a time, though. "
    "Try again."
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
        print(f"Letters guessed so far: {', '.join(guessed_letters)}", flush=True)
        return True

def main():

