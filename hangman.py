import random
import string

file = open("/Users/ciorneiedwinionatan/Desktop/PythonWantsome/Mine/Probleme_rezolvate/PROJECTS_FAIL/HANGMAN/wordlist.txt", 'r', encoding='UTF-8')
f1 = file.readlines()

def get_valid_word(f1):
    word = random.choice(f1)
    return word.upper()

def hangman():
    word = get_valid_word(f1)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    tries = 6
    
    while len(word_letters) > 0 and tries > 0:
        if tries == 6:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif tries == 5:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif tries == 4:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /       ")
            print("|             ")
            print("|             ")
        elif tries == 3:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif tries == 2:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif tries == 1:
            print("________      ")
            print("|      |      ")
            print("|      0      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")


        print('You have', tries, 'tries left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Current word: ', ' '.join(word_list) )
        
        user_letter = input("Guess a letter: ").upper()
       
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if used_letters in word_letters:
                word_letters.remove(used_letters)
            else:
                tries = tries - 1 
                print("Letter not in the word")

        elif user_letter in used_letters:
            print("you guessed that character")

        else:
            print("invalid input") 
    if tries == 0:
        print("________      ")
        print("|      |      ")
        print("|     😵      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("You are out of tries.The word was", word)
    else:    
        print('You guessed the word', word, '!')
hangman()