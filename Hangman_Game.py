import random
from time import sleep
import matplotlib.pyplot as plt
from engi1020.arduino.api import *# will need to add this Library for the use of Arduino usage for Button,Sound and LED, This package allows to python to run on arduino

#Step 2.1
def find_positions(letter, word):
    """Returns a list of positions where the letter appears in the word.
    Parameters
    - ---------
    letter : str
        A single character string representing the guessed letter.
    word : str
        A string representing the chosen word in which to find occurrences of the letter.
    Returns
    -------
    list of int
        A list of positions (indices) where the letter appears in the word.
    """
    position_list = []
    for i in range(len(word)):
        if word[i] == letter:
            position_list.append(i)
    return position_list


HANGMAN_PICS = [
'''
   +---+
   O   |
       |
       |
      ===''',
'''
   +---+
   O   |
   |   |
       |
      ===''',
'''
   +---+
   O   |
  /|   |
       |
      ===''',
'''
   +---+
   O   |
  /|\  |
       |
      ===''',
'''
   +---+
   O   |
  /|\  |
  /    |
      ===''',
'''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = [['python', 'java', 'ruby', 'html', 'css'],
         ['hangman', 'programming', 'computer', 'science'],
         ['openai', 'challenge', 'algorithm', 'datastructure']]   

History_n = []
History_s = []
#step 2.2
while True:
    user_name = input("Enter your Name : ")
    d_level = int(input("Choose your difficulty level: [0] - easy, [1] - medium, [2] - hard "))
    chosen_word = random.choice(words[d_level])
    print(chosen_word)
    print("The word has",len(chosen_word),"letters")
    pos_list = []
    for i in range(len(chosen_word)):
        pos_list.append("_")
    print(pos_list)
#step 2.3
    chances = 6
    guessed_word = ""
    while True:
        guess = input("Guess a Letter ! ")
        if len(guess) != 1 or guess.isalpha() == False:
             print("Invalid Input")
        elif guess in guessed_word :
            print("You already guessed that letter. Try again!")
        elif guess in chosen_word:
            guessed_word += guess
            #print(find_positions(guess, chosen_word))
            indices = find_positions(guess, chosen_word)
            for i in indices:
                pos_list[i] = guess
            print(pos_list)
            digital_write(4,True)#Activates LED
            buzzer_frequency(5,False)#Deactivates Buzzer
        else :
            chances -= 1
            print(HANGMAN_PICS[5-chances])
            print("Chances Left", chances)
            buzzer_frequency(5,300)#Activates Buzzer
            digital_write(4,False)#Deactivates LED
        if '_' not in pos_list:
            print("Congratulations!")
            break
        #step 2.4
        if chances==0:
            print("Game over! The word was:",chosen_word)
            break
    History_n.append(user_name)
    History_s.append(chances)
    
    #print( History_n,History_s)
    print("Press the button if you want to play again ")
    sleep(2) 
    if digital_read(6) == False : #The will give the user a chance to play again by holding the button down
        break
plt.bar(History_n,History_s)
plt.show()