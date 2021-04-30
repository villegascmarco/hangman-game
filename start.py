import os
import platform
import random
import unidecode

attempts=0

def is_linux():
    return platform.system() == 'Linux'


def clear_console():
    if is_linux():
        os.system('clear')
    else:
        os.system('cls')


def read_data():
    list_data = []
    with open('./data.txt', 'r', encoding='utf-8')as file:
        list_data = [line.strip() for line in file]

    return list_data

def increase_attempts():
    global attempts
    attempts+=1

    if attempts == 6: #hangman variable length -1
        return False
    else:
        return True

def get_hangman_ascii():
    hangman = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
    print(hangman[attempts])

def get_random_word():
    list_data = read_data()

    accented_string = random.choice(list_data)
    new_word = unidecode.unidecode(accented_string)

    return [letter for letter in new_word if letter != '\n']


def guess_word(word):
    guessed_word = '_'*(len(word))

    while True:
        guessed_word_list = [letter for letter in guessed_word]
        update_screen([guessed_word])
        letter = input('Ingrese una letra: ')

        try:
            indices = [i for i, x in enumerate(word) if x == letter]
            
            if (not len(indices)) and (not increase_attempts()):# increase_attempts() will be reach only when indices is empty
                break

            for i in indices:
                guessed_word_list[i]=letter
            guessed_word=''.join(guessed_word_list)
        except ValueError:
            pass

        if not '_'in guessed_word:
            break
    update_screen([guessed_word,'The word was '+''.join(word)])

def update_screen(arguments):
    clear_console()
    get_hangman_ascii()
    for argument in arguments:
        print(argument)

def run():
    clear_console()
    new_word = get_random_word()

    guess_word(new_word)


if __name__ == '__main__':
    run()
