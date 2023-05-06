HANGMAN_ASCII_ART = """
             _    _                                         
            | |  | |                                        
            | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
            |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | |  | | (_| | | | | (_| | | | | | | (_| | | | |
            |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/  """  # Open Screen of the game

print(HANGMAN_ASCII_ART)  # Open to the game

HANGMAN_PHOTOS = {
    "1": "x-------x",
    "2":
        """    x-------x
    |
    |
    |
    |""",
    "3":
        """    x-------x
    |       | 
    |
    |
    |""",
    "4":
        """    x-------x
    |       |
    |       0
    |       |
    |
    |""",
    "5":
        """    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |""",
    "6":
        """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""",
    "7":
        """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


def print_hangman(num_of_tries):
    """
    The function prints the correct disqualification of the course of the game
    :param num_of_tries: The parameter indicates the number of disqualifications of the player
    :type num_of_tries: int
    :return: integer 
    :rtype: int
    """

    print(HANGMAN_PHOTOS[str(num_of_tries)])


def choose_word(file_path, index):
    """
    The function gets a path to the file and a number which is an index
    :param index: is index
    :type index: str
    :param file_path: Parameter gets a number
    :type file_path: int
    :return: string
    :rtype: str
    """
    file_open = open(file_path, 'r', encoding='utf-8')
    file_open2 = file_open.read()
    file_split = file_open2.split(" ")
    secret_word = file_split[index - 1]
    file_open.close()
    X = "_ "

    print(X * len(secret_word))  # Create a game board, and desplay _ acoording to the secret word length
    return secret_word

file_path = input("Enter file path: ")
index_num = input("Enter index: ")
index = int(index_num)
secret_word = choose_word(file_path, index)


def print_sorted_list(old_letters_guessed):
    """
    A function that receives a string, and checks if the 
    element is equal to the last element in the array - 
    just print the element otherwise it will not be necessary "->" at the end
    :param old_letters_guessed: Just a printable list
    :type old_letters_guessed: list
    :return: list
    :rtype: str or list
    """
    sorted_list = sorted(old_letters_guessed)
    for i in sorted_list:
        # if i equals the last element in the array - print only the element
        # otherwise there will be unneeded -> at the end
        if i == sorted_list[-1]:
            print(i)
        else:
            print(i, end=' -> ')


def check_valid_input(letter_guessed: object, old_letters_guessed: object) -> object:
    """
    The function checks if the input is valid.
    With the input in the letters of the alphabet
    And receiving one letter then it returns true
    If not then it returns False
    :param letter_guessed: Receives user input
    :type letter_guessed: str
    :param old_letters_guessed: The list holds the letters the player has guessed so far
    :type old_letters_guessed: list
    :return: True and False
    :rtype: bool
    """

    if len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letters_guessed or letter_guessed in secret_word:
        return True
    ## check if input is valid
    ## input is valid if it's 1 alphabet letter and not already in the old_letters_guessed
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The Boolean function that returns truth if all the letters 
    that make up the secret word are included in the list of letters 
    that the user guessed. Otherwise, the function returns a lie.
    :param letter_guessed:
    :param old_letters_guessed: The list holds the letters the player has guessed so far
    :type old_letters_guessed: list
    :return: True and False
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print("X")
        print_sorted_list(old_letters_guessed)

        return False, old_letters_guessed

    else:
        old_letters_guessed.append(letter_guessed)
        return True, old_letters_guessed


def show_hidden_word(secret_word, old_letters_guessed):
    """
    This is a function that returns a string which consists of letters and lower hopes.
    The string displays the letters from the old_letters_guessed list that are in the secret_word string in their appropriate position,
    and the rest of the letters in the string (which the player has not yet guessed) as underlines.
    This is a function that returns a string which consists of letters and lower hopes. 
    The string displays the letters from the old_letters_guessed list that are in the secret_word string in their appropriate position,
    and the rest of the letters in the string (which the player has not yet guessed) as underlines.
    :param secret_word: The secret_word parameter is a type of string that contains the word that needs a secret
    :type secret_word: str
    :param old_letters_guessed: The list holds the letters the player has guessed so far
    :type old_letters_guessed: list
    :return: string 
    :rtype: str
    """
    clue = ""
    x = "_ "

    for letter in secret_word:
        if letter in old_letters_guessed:
            clue = clue + letter
        else:
            clue = clue + x
    return clue


def check_win(secret_word, old_letters_guessed):
    """
    This is a Boolean function that returns truth if all the,
    letters that make up the secret word are included in the list of letters that,
    the user guessed.
    Otherwise, the function returns a lie.
    :param old_letters_guessed:
    :param secret_word: This is the word that should be used for a snake,
    which passes as an argument for a execution function.
    :type secret_word: str
    :return: True or False
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def main():


    num_of_tries = 1
    print_hangman(num_of_tries)

    old_letters_guessed = []
    print("Let’s start!")

    while True:

        print(show_hidden_word(secret_word, old_letters_guessed))

        while True:
            letter_guessed = input("Guess a letter: ").lower()
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
            check_valid_input(letter_guessed, old_letters_guessed)
            break

        if check_valid_input(letter_guessed, old_letters_guessed):
            num_of_tries = num_of_tries + 1
            print_hangman(num_of_tries)

        if check_win(secret_word, old_letters_guessed):
            print(show_hidden_word(secret_word, old_letters_guessed))

            print("WIN")
            break

        if num_of_tries == 7:
            print(show_hidden_word(secret_word, old_letters_guessed))

            print("You failed")
            break


if __name__ == "__main__":
    main()
