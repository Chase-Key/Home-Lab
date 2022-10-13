
import random


#   User guess computer's number
import string


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and x: '))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        if guess > random_number:
            print("Sorry, guess again. Too high.")
    print("\n\n!!!!!CONGRATS!!!!! You have guessed the random number!")


#   Computer guesses your number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low   # could also be high cause low = high
        feedback = input("Is " + str(guess) + " too high? (H) Is guess too low? (L) Is guess correct? (C)?")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess - 1

    print("\n\nYay! The computer guessed your number correctly!")


#    Rock, Paper, Scissors
def play():
    user = input("What's your choice? \n\n(r) for rock, (p) for paper, (s) for scissors\n(r,p,s):")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return ("\n\nIt's a tie!")

    if is_win(user, computer):
        return ("\n\nYou won!")

    return ("\n\nYou lost!")

def is_win(player, computer):
    #return true if player wins
    if (player == 'r' and computer == 's' or player == 's' and computer == 'p' or player == 'p' and computer == 'r'):
        return True

                                 ### GAMES ###
#guess(1000)             #   Guess Computer's Number
#computer_guess(1000)    #   Computer guesses your' Number
#print(play())          #   Rock, Paper, Scissors

import requests
lives = 6
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()
#print(WORDS)
def get_valid_word(WORDS):
    word = random.choice(WORDS)
    while '-' in word or ' ' in word:
        word = random.choice(WORDS)

    return word.upper()

def hangman():
    word = get_valid_word(WORDS)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #getting user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that character. PLease try again.")
        else:
            print("Invalid character. Please try again.")
    # gets here when len(word_letters) == 0


#hangman()


















