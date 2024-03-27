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