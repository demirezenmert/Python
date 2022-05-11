from distutils.log import error
from itertools import count
import time
from time import sleep
import random




    


def welcome():
    print('Welcome to Hangman Game by Mert Demirezen')
    player_name = input('Enter your name: ')
    print(f'Hello {player_name}! Best of luck')
    sleep(2)
    print("The game is about to start!\nLet's play Hangman!")
    sleep(3)

def wordPicker():
    try:
        with open ('word.txt','r') as file:
            words = file.readlines()
        if len(words) == 0:
            words = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]            
    except:
        words = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    word = random.choice(words)
    word = word.rstrip()
    return word
        
def main():
    global display  
    global word_pick
    global word
    global length
    global limit 
    global play_game
    global already_guessed
    global count
    already_guessed = []
    limit = 5
    count = 0
    word = wordPicker()
    word_pick = word
    length = len(word)
    display = '_' * length
    play_game = ''

    
    
def play_loop():
    global play_game
    play_game = input('Do you want to play again? \n')
    while play_game not in ['y','yes','YES','Yes','n','no','No','NO']:
        play_game = input('Do you want to play again? \n')
    if play_game in ['y','yes','YES','Yes']:
        main()
    elif play_game in ['n','no','No','NO']:
        print('Thanks for playing! See soon again!')
        exit()

def hangman():
    global word
    global word_pick
    global display
    global count
    global already_guessed
    limit = 5
    guess = input(f'This is the hangman word: {display}\n Enter your guess letter: \n')
    guess = guess.strip()
    if len(guess) >= 2 or len(guess) == 0 or guess <= '9' or guess in [';',':','@',',']:
        print('Invalid input! Try a letter!\n')
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display)
    elif guess in already_guessed:
        print('Already guessed this leter \nTry another letter.\n')
    else:
        count += 1

        if count == 1:
            sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print(f"The word was: {word_pick} Your correct guesses {already_guessed}")
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()

    
if __name__ == '__main__':
    welcome()
    main()
    hangman()