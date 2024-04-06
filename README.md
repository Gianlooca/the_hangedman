# the_hangedman

(Developer: Gianluca Zimmatore)

## Introduction ##
**the_hangedman** is an online is a Python terminal version of the classic hangman game. The aim of the game, as we know, is to guess a secret word (randomply chosen by the computer from a specific list) letter by letter, but in a range of maximum six attempts. If you guess the word within this range you win, otherwise you lose.

![Mockup image](docs/mockup_hangedman.png)

[Live webpage](https://the-hangedman-9d230e2d51fc.herokuapp.com/)
<br>
<br>
<br>

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [How To Play](#how-to-play)
    2. [User Stories](#user-stories)
        1. [Users](#users)
        2. [Site Owner](#site-owner)
3. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Game Logic General Idea](#game-logic-general-idea)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
    1. [Title](#title)
    2. [Menu](#menu)
        1. [Start](#start)
        2. [Instructions](#instructions)
    3. [Ask Username](#ask-username)
    4. [Actual Game Display](#actual-game-display)
    5. [Game Over](#game-over)
        1. [Win](#win)
        2. [Lose](#lose)
    6. [Exit Game Message](#exit-game-message)
6. [Game Logic Less General Idea](#game-logic-less-general-idea)
7. [Bugs](#Bugs)
    1. [Fixed Bugs](#fixed-bugs)
    2. [Unfixed Bugs](#unfixed-bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
    1. [General References](#general-references)
    2. [Code](#code)
10. [Acknowledgements](#acknowledgements)

## Project Goals 

### User Goals
- Playing a classic hangman game. 
- Finding easily the instructions about the game.
- Receiving clear information about what's happening during a game,
- Playing easily a new game (or exiting the program with the same ease)

### Site Owner Goals
- Providing a good UX/UI.
- Providing a fully working videogame with no bugs.
- Providing clear information about what to do in order to play.
<br>
<br>
<br>

## User Experience

### How To Play
1. The aim of the game is to guess a random word letter by letter;
2. To guess, type a letter (no punctuation, spaces or numbers are allowed) and press enter;
3. If you guess correctly, the letter will be revealed in its exact position in
   the secret dashed word (each dash is a letter, so you can know before starting to play how many letters you have to guess)
4. If you guess incorrectly, you will lose a "life" and the hanged man will
   start to build.
5. You have 6 "lives", that is 6 attempts, to guess the correct word: head, torso, two arms and two
   legs
6. The word that you have to guess can be everything: a singular name, a plural
   name, a verb, a past participle, etc.

*By the way, you can find all the instructions directly on the [live webpage](https://the-hangedman-9d230e2d51fc.herokuapp.com/) of this project or, if you want to have more general information about it, in the Wikipedia page about the [hangman game](https://en.wikipedia.org/wiki/Hangman_(game))*
<br>
<br>

### User Stories

#### Users 
1. As a user, I want to know quickly what the website is about.
2. As a user, I want to easily understand how to play.
3. As a user, I want to see if I am doing something wrong and what to do to correct myself.
4. As a user, I want to be able to play again easily.

#### Site Owner 
1. As the site owner, I want users to understand immediately what the site is about.
2. As the site owner, I want to avoid any possible bug to break the game.
3. As the site owner, I want to give a special taste to a perhaps "too classic" game with some special "handmade" ASCII art.
<br>
<br>
<br>

## Design

### Design Choices
The terminal emulator provided by the Code Institute (and, more in general, the fact that the purpose of this project is just to "build a command-line application") kind of minimised the possibilities of creating my own design. I could have used libraries such as colorama to differentiate the output with colours, but I preferred to give a soul to the game by using customized (and sometimes humorous, depending on the point of view, of course) output, in advance and in response to users' inputs, while on a visual level keeping a sketchy, classic, "terminal" style, sealing it with the help of pieces of ASCII art that I did myself (which can be seen in the main title - showing up as the user starts a new game or exits the program - and in the menu "board"). In addition to this, I created and charged a favicon showing the quite recognizable shape of a gibbet.

### Game Logic General Idea
A design feature is, in my personal sense of the word, also the way the game logic has been thought - and designed, in fact. We're all aware of the rules of the hangman game (you can find all the instructions directly on the [live webpage](https://the-hangedman-9d230e2d51fc.herokuapp.com/) of this project or in the Wikipedia page about the [hangman game](https://en.wikipedia.org/wiki/Hangman_(game))); in our chase, a flowchart describing the general game logic it's probably more descriptive (further on, in another section, we will see a similar flowchart integrating also functions and user inputs).

![General Game Logic Flowchart](docs/flowcharts/general-flowchart-hangedman.png)
<br>
<br>
<br>

## Technologies Used

### Languages
- HTML
- Javascript
- Python

### Frameworks & Tools
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Gitpod](https://gitpod.io/)
- [Heroku](https://www.heroku.com/)
- [Am I Responsive?](https://ui.dev/amiresponsive)
- [Favicon](https://favicon.io/)
- [Snipping Tool](https://apps.microsoft.com/detail/9MZ95KL8MR0L?hl=en-US&gl=US)
- [Paint](https://www.microsoft.com/it-it/windows/paint)
- [Lucidchart](https://www.lucidchart.com/pages/)
- [Replit](https://replit.com/)
- [Google](https://www.google.com/)
- [W3C Markup Validation Service](https://validator.w3.org/)
- [CI Python Linter](https://pep8ci.herokuapp.com/)
<br>
<br>
<br>

## Features

*for input validation and error checking we link to the general [TESTING.md](TESTING.md) file.*

### Title
- This feature is displayed automatically as soon as the user runs the program, starts a new game or decides to exit the game. It consists of a three levels structure, all three an example of (autographic) ASCII art:
    1. The top levels it's some sort of acronym (not exactly an acronym) with the three letters: "h", "G" and "n" (from the far left, center and right of the word "hangman") in a bidimensional way (the "h" has its shadow pushing leftwards, the "G" towards the center and the "n" rightwards). Each letter is "coloured" with the same letter but capitalized;
    2. The actual title of the game "the hangedman", written in a more readable way;
    3. a visual logo, to let the user understand (once again, if needed) what the game is about: the drawing of gallows with an hanging man saying: "life is but a slipknot", as a motto of the game.

    ![Title Screenshot](docs/features/title-hangedman.png)
<br>
<br>

### Menu
- This feature is displayed as well automatically as soon as the user either runs the program or starts a new game. As the Title, it's an example of autographic ASCII art. We will show its general appearence (constituted by some kind of billboard, from which four sketchy men are hanging) and briefly explain its only two (self-evident, actually) functions:

![Menu Screenshot](docs/features/menu-hangedman.png)

#### Start
- If the user presses the letter "s/S" and then Enter, a new game starts. We will see a few screenshots from the game further on.

#### Instructions
- If the user presses the letter "i/I" and then Enter, the instructions of the hangman game will be displayed, together with some vague suggestions about which kind of input the terminal will accept as valid and which kind of words are potentially to be guessed. After reading the instructions, the user has to press Enter to go back to the Menu (the ASCII art won't be displayed this time):

![Instructions Screenshot](docs/features/instructions-hangedman.png)
<br>
<br>

### Ask Username
- To be precise, after the user presses the letter "s/S", before a new game begins, the program asks his/her name. The user then will input the name, which from then on will be displayed with the first letter capitalised (no matter if the user actually had the consideration of writing it in that way):

![Ask Username Screenshot](docs/features/ask-username-hangedman.png)
<br>
<br>

### Actual Game Display
- Once the game starts, as already said, the user will have to guess the right letters. Hereafter we'll just show three of screenshots from the gameplay (the empty gallows and after the first and the fourth mistake), just to have an idea of the body of the Hangedman building after missing a few "lives". You'll have time to see the whole game by playing it. And, as you can see, the list of the letters guessed so far, no matter if correctly or incorrectly guessed, is displayed close to the word to guess, that is to the user eyes, for a better UX:

![Actual Game Display Zero Screenshot](docs/features/actual-game-display-zero-hangedman.png)

![Actual Game Display One Screenshot](docs/features/actual-game-display-one-hangedman.png)

![Actual Game Display Four Screenshot](docs/features/actual-game-display-four-hangedman.png)
<br>
<br>

### Game Over
- The game will be over either when the user guesses correctly all the letters in the secret word (that is, by winning the game) or when the user didn't guess the word but wasted his/her 6 "lives" trying to guess (that is, by losing the game). Two different message will be displayed in either of the two cases, but in the end will be always offered to the player the chance to play another game (by inserting the letter "y/Y" and Enter), or to exit the game if he/she's just fed up of hanging bodies.

#### Win
![Win Screenshot](docs/features/game-over-win-hangedman.png)

#### Lose
![Lose Screenshot](docs/features/game-over-hangedman.png)
<br>
<br>

### Exit Game Message
- If the user wants to leave the game, the following message will be displayed, along with the Title (as mentioned before):

![Exit Game Screenshot](docs/features/exit-game-hangedman.png)
<br>
<br>
<br>

## Game Logic Less General Idea

I wanted to call this section "Game Logic Less General Idea" because here the logic of the game won't be described very specifically: a specific description may only come by putting in comparison the actual code, the docstrings describing in general what the functions are supposed to do and the comments to highlight certain steps which may not be clear enough and the following flowchart:

![Less General Game Logic Flowchart](docs/flowcharts/functions-and-less-general-game-logic-hangedman.png)

Basically, all the game is governed by the main() function and, specifically, by a while loop inside it; all the other functions are called inside it. For a better readability, I created another Python file with all the constants which I imported at the beginning of our run.py file (together with the random and the string modules, only used before the actual game starts, that is: to "eject" punctuation, spaces or eventual numbers from our source of words and to choose a random one from this conglomerate). I tried to keep the program as neat and atomical as possible, but I am sure that it could be refactored and streamlined.
<br>
<br>
<br>

## Bugs

### Fixed bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| The ASCII arts (the seven stages, saved in strings, inside the constant HANG_STAGE) of the hangedman were returning an error and one could not visualize them correctly in the console | I had to transform those strings in raw strings. *(For the reference to this solution we'll put a couple links in the Credits section - inside the Code chapter)* |
| When (before it was in the main() function, then I created a small end_game() function for this) asking the user if he/she wanted to play another game and then to insert 'y' or 'n', even if I was using the correct input the program was returning the "else" message, that is it was responding as after an invalid input | Mistakenly, that's what I wrote: play_again = input("Do you want to play again?\nPlease enter 'y' and ENTER for yes or 'n' and ENTER for no.\n").upper(). That means that even if I inserted the lowercase 'y' or 'n', it was transformed into uppercase. I just had to change the upper() into lower() method. |
| At some point of the developing I had problems with the display of the Hangedman; it either was start to build after my second incorrect guess (but the amount of "lives" were the same, so I couldn't see its body completely displayed and hanged) or giving me a GUESS more, since I tried to fix the bug by putting GUESSES == 1, hence showing immediately the full body hanged after the first mistake | I managed to solve the issue by putting the if GUESSES == 0 or word_in_display == word_in_game: / game_over = True / break block of code before asking to the user to guess a new letter, since before it was doing the exact opposite, that is: asking for a new letter before checking if the condition of game_over was actually True. |
| Once refactored the main() function, since I added and created an end_game() function, after having ended one game it gave me an IndexError related to the GUESSES constant, or rather to how I was using it to index the HANG_STAGE list. | I sorted this out by adding the code block "GUESSES = len(HANG_STAGE)": this Resets the constant GUESSES at the beginning of each game, so the constant won't go below zero after the first defeat and it's refreshed at any new game. |
| I wanted to use the update_guessed_letters() function to actually display a list of the letters guessed (correctly or incorrectly) by the user and display it only after the ASCII art of the Hangedman was printed at each round, since it was displayed even before it (hence twice, which was redundant and not user friendly) | I ousted the update_guessed_letters() function of that role and just printed the list called guessed_letters from within the main() function. |
| I needed a bigger terminal window in order to show all the ASCII art of the hangedman and of the Title. | I changed the script inside the index.html, inside the var variable and changed the number of rows. Then, I also played within the layout.html shrinking a bit the margin of the button, in order to have more space without scrolling the page. |

### Unfixed Bugs

- I didn't manage to make the website responsive: I tried to add media queries for screens smaller than 768 * 1024 pixels in the layout.html, defining a specific height and width in % in order to not distort the image (and using a non-fixed unit of measurement) and created an (apparently) working JavaScript function in the index.html to change the number of rows under certain conditions, but it didn't work.
- On Google Chrome I noticed with my mentor that the underscores (which, in fact, I changed into dashes hoping for a different displaying) of the secret word weren't displayed in the deployed website. On Edge there are no problems, though, and strangely I couldn't notice the same problem on my phone (which uses Chrome as a browser).
- I couldn't insert spaces after each letter in the word to guess. That's definitely an aim for a future implementation of the game.
<br>
<br>
<br>

## Deployment

The project was deployed to Heroku, a platform designed to host dynamic websites where backend languages are used. I had to follow all these steps, since I was totally new to Heroku:

1. Log in to Heroku.
    - If you don't have one, as I didn't, you can create an account by clicking on the purple "Sign up for free button" in the homepage, then fill up the form (selecting also your primary development language, in this case Python) and click on "Create free account". Heroku will send a confirmation email, so you'll need to open it and click on the provided link. Once done that, you'll be redirected on another page to create your password; when you're happy with that, you can click “Set password and log in”. We finally have a welcome message and we'll need to the only button we'll see in that page to proceed. We'll need to accept the terms of service of Heroku by clicking, once again, on the only "accept" button we'll see in that page. We'll finally be in our dashboard.
2. If you're a student of the Code Institute (or of another school giving some kind of discount to use Heroku) you'll need to activate your GitHub Student Developer Pack. Then, you'll need to:
    1. Navigate to https://www.heroku.com/github-students;
    2. Click “Get the student offer”;
    3. Login with Heroku;
    4. Click “Verify with GitHub”;
    5. Click “Authorize Heroku”;
    6. In order to receive the Heroku credits, payment details are required. If you have already supplied details, continue by clicking “Verify my billing information” and skip to step 7. If, however, you have not provided any details, click “Add a credit or debit card to your account now”;
    7. In the new tab, click “Add credit card”. Note that this doesn’t have to be a credit card, a debit card will work just as well (even if for me a debit card didn't work);
    8. Enter your payment details as requested and then head back to the Heroku sign up process (you may need to refresh the page for Step 2 to validate). If you closed the tab, [open it up again here](https://www.heroku.com/auth/login);
    9. Enter your details, ensuring to put “Code Institute” as your School name, heed the warning and then click “Send”;
    10. Read Heroku’s terms and click “Agree” to continue;
    11. A thank you message will be shown, indicating that it can take up to 24 hours for the request to be processed;
    12. When the confirmation email comes through from Heroku, you can check your credits via https://dashboard.heroku.com/account/billing. Here you should find that $156.00 of credits have been applied to your Platform Credits. It can take a while for the dashboard to update, so please wait the full 24 hours before contacting Heroku support in the event of any errors. If you don't get your Heroku credits within 24 hours. Raise a ticket with Heroku [here](https://www.heroku.com/support) and they can fix that for you.
3. On the dashboard, click the “Create new app” (app stands for "web application") purple button. Click instead on the "new" white button on the top right and select "create new app", if you already have at least one app created;
4. Enter the app name. I named mine ultimate-hangman (this has to be unique, so you may use a bit of your time here in order to find the appropriate name);
5. Once Heroku accepts the app name select your region;
6. Click the purple "Create app" button;.
7. This will bring you to a page with all the information for setting up  your app. On the top left of the page you'll see several voices: first of all, navigate to the "Settings" tab and scroll down to the "Config Vars" (also known as "Environment Variables") section.
8. Click the button labeled "Reveal Config Vars", then enter the key as Port, the value as 8000 and click the purple "Add" button. If you have sensitive data to store that needs to be kept secret and which, consequently, aren't stored into the GitHub repository, you can add another Config Var.
9. Scroll down to the Buildpacks section of the Settings page, click the button labeled "Add buildpack", select Python, and click on "Save";
10. Repeat step 10 but this time add Node.js instead of Python. (Remember to keep the buildpacks in the correct order, Python first and Node.js second. If they're the other way around you  can click and drag them to change the order.);
11. Scroll back to the top of the Settings page, and navigate to the Deploy tab.
12. From the deploy tab select Github as the deployment method.
13. Confirm you want to connect to GitHub.
14. Search for the repository name; write the correct name, click on the purple "Search" and then click the on the white "Connect" button below next to the intended repository.
15. From the bottom of the deploy page select your preferred deployment type by following one of the steps below:
    1. Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to GitHub (which I haven't chosen, but it's much more practical)
    2. Or you can choose the Manual Deploy using the Deploy Branch option. If you choose this, you have to deploy every time (it's not automatically connected to GitHub); after each process, you can click on the "View" button in order to open and check your deployed website version.
<br>
<br>
<br>

## Credits

### General References
I will mention just a few benchmarks for my general approach to Python:
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/);
- [This italian website](https://www.programmareinpython.it/corsi-e-lezioni-python-dal-nostro-canale-youtube/) with free material and links to their YouTube videos;
- [Real Python Tutorials](https://realpython.com/);
- [Datacamp](https://www.datacamp.com/) in general (I subscribed to their 3 months free trial, since the GitHub Student Pack was given to me by Code Institute), their Python introductive course (which I am attending while studying here at CI) and in particular [this article](https://www.datacamp.com/tutorial/python-oop-tutorial) to understand a bit better the OOP (action which is still in progress...);
- [This archive](https://gasei.gitbook.io/sei/intro) is also a nice resource and I've been reading a few things from it;
- I stepped into [this other forum](https://discuss.python.org/) in the last days of my development phase, it would have been helpful to know it before, but it's still worth to mention here.

As usual, as a guide to write a complete and detailed README.md, I stick always to the work of [Ana Runje](https://github.com/4n4ru) in her [Bodelschwinger Hof Project](https://github.com/4n4ru/CI_MS1_BodelschwingherHof), but this time I also had the example of my colleague [Ilyascan OIgun](https://github.com/ilyasolgun11) in [his README.md file for his beautiful project](https://github.com/ilyasolgun11/hangman/blob/main/docs/README.md), which helped me a lot mostly when it came about the "Deployment" section.
<br>

### Code

- To solve any problem with the print of the ASCII art pieces, I have found two instructive sources: [a stack overflow discussion](https://stackoverflow.com/questions/23623288/print-full-ascii-art) and [this article about raw strings](https://www.digitalocean.com/community/tutorials/python-raw-string);
- 