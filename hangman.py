from ctypes.wintypes import WORD
from itertools import count
import random
from sys import displayhook 
import time
from wsgiref.util import guess_scheme 

print ("Welcome to the hangman game")
name = input("Please input your name: ")
print("Hello " + name + ", have fun!")

def main():
    global count
    global display
    global word
    global guessed 
    global lenght 
    global play_game
    words = ['happy','clock','edible','untouchable','table','keyboard','town','stupid','workplace']
    word = random.choice(words)
    lenght = len(word)
    count = 0
    display = '*' * lenght
    guessed = []
    play_game = ""
    
def play_loop():
    global play_game
    play_game= input("Do you want to play again? y = yes n = no \n")
    while play_game not  in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thank for playing!")
        exit()

def hangman():
    global count
    global display
    global word
    global guessed 
    global play_game
    global lenght
    limit = 10
    

    guess = input("This is the word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("invalid Input, Try a letter")
        hangman()
    elif guess in word:
        guessed.extend([guess])
        while guess in word:
            index = word.find(guess)
            word = word[:index] + "*" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
        print("You guessed correctly. The word is: " + display + ".\n")
        hangman()
    elif guess in guessed:
        print("The letter is already been used. (Used letters: " + ', '.join(guessed) + ")\n")
    else:
        guessed.extend([guess])
        count += 1
    if count == 1:
        time.sleep(1)
        print("  _____ \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
    elif count == 2:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
    elif count == 3:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  | \n"
        "  | \n"
        "  | \n"
        "  | \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
    elif count == 4:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  |   | \n"
        "  |  \n"
        "  | \n"
        "  | \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
    elif count == 5:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  |   | \n"
        "  |   0\n"
        "  | \n"
        "  | \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
    elif count == 6:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  |   | \n"
        "  |   O \n"
        "  |   | \n"
        "  |   \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
    elif count == 7:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  |   | \n"
        "  |   O \n"
        "  |  /| \n"
        "  |   \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
    elif count == 8:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  |   | \n"
        "  |   O \n"
        "  |  /|\ \n"
        "  |    \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
    elif count == 9:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  |   | \n"
        "  |   O \n"
        "  |  /|\ \n"
        "  |  / \n"
        "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
    elif count == 10:
        time.sleep(1)
        print("  _____ \n"
        "  |   | \n"
        "  |   |\n"
        "  |   | \n"
        "  |   O \n"
        "  |  /|\ \n"
        "  |  / \ \n"
        "__|__\n")
        print("Wrong guess. You are hanged!!!\n")
        print("The word was:",guessed ,word)
        play_loop()
    if word == '*' * lenght:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()
        
main ()
hangman()