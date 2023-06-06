
#Binod Chalise #Kathmandu, Nepal
import random
def login():
    username="admin"
    password="Namaste"
    user=input("username: ")
    passw=input("password: ")
    if user==username and passw==password:
        print("Hurray!! login successfully")
    else:
        print("Sorry!! Try again")
        login()
login()
def play_hangman():
    word_list=['America','Canada','Australia','Nepal','China','Japan']
    word=random.choice(word_list).upper()
    guessed_letters=[]
    tries=10
    while True:
        hidden_word=''
        for letter in word:
            if letter in guessed_letters:
                hidden_word +=letter +''
            else:
                hidden_word +='-'
       
        print('Guess the word: ', hidden_word)
        print('Gussed letters: ', guessed_letters)
        print('Tries remaining: ', tries)

        if '-' not in hidden_word:
            print('Congratulations! You guessed the word: ',word)
            break
        if tries==0:
            print('Game over! The word was: ',word)
            break
        guess=input('Enter a letter: ').lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print('You already guessed that letter.')
            elif guess in word:
                print('Correct guess!')
                guessed_letters.append(guess)
            else:
                print('Wrong guess!')
                tries -= 1
                guessed_letters.append(guess)
        else:
            print('Invalid input. Please enter a single letter.')

        print()

play_hangman()
    

