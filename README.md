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
    3. [Input Messages](#input-messages)
    4. [Automatic Responses](#automatic-responses)
6. [Testing](#testing)
    1. [HTML Validation](#HTML-validation)
    2. [PEP8](#PEP8)
    3. [Testing user stories](#testing-user-stories)
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

## User Stories

### Users 
1. As a user, I want to know quickly what the website is about.
2. As a user, I want to easily understand how to play.
3. As a user, I want to see if I am doing something wrong and what to do to correct myself.
4. As a user, I want to be able to play again easily.

### Site Owner 
1. As the site owner, I want users to understand immediately what the site is about.
2. As the site owner, I want to avoid any possible bug to break the game.
3. As the site owner, I want to give a special taste to a perhaps "too classic" game with some special "handmade" ASCII art.
<br>
<br>
<br>

## Design

### Design Choices
The terminal emulator provided by the Code Institute (and, more in general, the fact that the purpose of this project is just to "build a command-line application") kind of minimised the possibilities of creating my own design. I could have used libraries such as colorama to differentiate the output with colours, but I preferred to give a soul to the game by using customized (and sometimes humorous, depending on the point of view, of course) output, in advance and in response to users' inputs, while on a visual level keeping a sketchy, classic, "terminal" style, sealing it with the help of pieces of ASCII art that I did myself (which can be seen in the main title - showing up as the user starts a new game or exits the program - and in the menu "board").

### Game Logic General Idea
A design feature is, in my personal sense of the word, also the way the game logic has been thought - and designed, in fact. We're all aware of the rules of the hangman game (you can find all the instructions directly on the [live webpage](https://the-hangedman-9d230e2d51fc.herokuapp.com/) of this project or in the Wikipedia page about the [hangman game](https://en.wikipedia.org/wiki/Hangman_(game))); in our chase, a flowchart describing the general game logic it's probably more descriptive (further on, in another section, we will see a similar flowchart integrating also functions and user inputs).

![General Game Logic Flowchart](docs/flowcharts/general-flowchart-hangedman.png)
