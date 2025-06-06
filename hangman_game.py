import random
word_list = [
    "Umbrella",
    "Galaxy",
    "Enigma",
    "Harmony",
    "Serendipity",
    "Velocity",
    "Quantum",
    "Maverick",
    "Epiphany",
    "Zephyr",
    "Nexus",
    "Solstice",
    "Euphoria",
    "Cascade",
    "Luminescence",
    "Paradox",
    "Nebula",
    "Odyssey",
    "Zenith",
    "Mirage"
]
def get_word():
    Word = random.choice(word_list)
    return Word.upper()
Word = get_word()
Character = []
for word in Word:
    Character.append(word)
def Game(word):
    word_completion = Character
    correct_letters = []
    max_tries = 6
    tries = 0
    while tries < max_tries:
        if word in Word:
            


def displayHangman(stage):
    hangman_stages = [
        '''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        ========='''
    ]
    
    return hangman_stages[stage]
