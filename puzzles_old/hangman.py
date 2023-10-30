import os

def hangman(word: str, current_state: int = -1, current_guess: list = [], guessed_letters: list = [], message: str = None, game_active: bool = True):
    # variables
    global states
    if not len(current_guess):
        current_guess = ['_' for c in word]

    # clear console
    os.system('cls' if os.name == 'nt' else 'clear')

    # start game or print message
    if not len(guessed_letters) and not message:
        game_active = True
    elif message:
        print(message + ('\n' if current_state < 0 and game_active else ''))

    # print state if an incorrect letter was guessed
    if current_state > -1:
        print(states[current_state])

    # print guessed letters if game active, if not handle exit
    if game_active:
        print(' '.join(current_guess) + '\n')
    else:
        return

    # input letter
    letter = input('Enter a letter to guess or type "exit" to exit the game: ')
    letter = letter.upper().strip()

    # validate exit
    if letter == 'EXIT':
        message = 'Successfully exited the game'
        game_active = False

    # validate letter
    elif len(letter) != 1 or not letter.isalpha():
        message = 'Please enter a valid letter'

    # validate if letter already guessed
    elif letter in guessed_letters:
        message = f'You already guessed the letter: {letter}'

    # if letter in word, replace '_' with letter
    elif letter in word.upper():
        message = f'Correct guess, the guessed the letter: {letter} is in the word'
        for i, c in enumerate(word.upper()):
            if c == letter:
                current_guess[i] = letter

        # win game if word complete
        if '_' not in current_guess:
            message = 'You correctly guessed the word!'
            game_active = False

        # add letter to guessed letters
        guessed_letters.append(letter)

    # if letter not in word, check if game over or up state
    else:
        message = f'Wrong guess, the guessed the letter: {letter} is not in the word'
        if current_state + 2 < len(states):
            current_state += 1
        else:
            current_state += 1
            message = f'You weren\'t able to guess to word!\nThe word was: {word.upper()}'
            game_active = False

        # add letter to guessed letters
        guessed_letters.append(letter)

    # repeat cycle
    hangman(word, current_state, current_guess, guessed_letters, message, game_active)


# states
states = [
    # state 1
    '''
==========
    ''',
    # state 2
    '''
    |
    |
    |
    |
    |
   /|\\
==========
    ''',
    # state 3
    '''
    +---+
    |/
    |
    |
    |
   /|\\
==========
    ''',
    # state 4
    '''
    +---+
    |/  |
    |
    |
    |
   /|\\
==========
    ''',
    # state 5
    '''
    +---+
    |/  |
    |   O
    |
    |
   /|\\
==========
    ''',
    # state 6
    '''
    +---+
    |/  |
    |   O
    |   |
    |
   /|\\
==========
    ''',
    # state 7
    '''
    +---+
    |/  |
    |   O
    |  /|
    |
   /|\\
==========
    ''',
    # state 8
    '''
    +---+
    |/  |
    |   O
    |  /|\\
    |
   /|\\
==========
    ''',
    # state 9
    '''
    +---+
    |/  |
    |   O
    |  /|\\
    |  /
   /|\\
==========
    ''',
    # state 10
    '''
    +---+
    |/  |
    |   O
    |  /|\\
    |  / \\
   /|\\
==========
    ''',
]