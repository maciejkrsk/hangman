#TO DO LIST
#AT THE BOTTOM
#OF THE DOC


class Hangman:
    import random
    from typing import List,Union
    import re

    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    #list of string
    word_to_find = []
    lives = 5

    correctly_guessed_letters=[] 
    wrongly_guessed_letters = []
    turn_count = 0
    error_count = 0

    def __init__(self):
        self.possible_words
        self.word_to_find
        self.lives
        self.correctly_guessed_letters
        self.wrongly_guessed_letters
        self.turn_count
        self.error_count
        
    #done
    def well_played(self):
        print(f"You found the word : {self.word_to_find}, in  {self.turn_count} turns with {self.error_count} errors!")
    
    
    #asks the ^player to enter a letter, if guessed one, add to correctly, else to error
    def play(self):
        invalid_input = True
        #Checks user input and stays in a loop until user complies with the rules.
        print("Enter a letter")
        while invalid_input:
            
            user_input = str(input())
            if len(user_input)>1:
                print("More than one character detected.")
            elif self.re.match('[0-9]| ',user_input):
                print("No numbers or empty characters allowed.")
            else:
                invalid_input=False
                
        #if the player entered a valid char ->
        #can eventually break the loop if valid
        
        #creating a variable that ensures user does not lose points at the end of the loop if found
        found_at_least_one = False
        self.turn_count+=1
        i=0
        for letter in self.word_to_find:
            
            if letter == user_input:
                #print(f"found {letter} at pos {i}")
                self.correctly_guessed_letters[i]=letter
                found_at_least_one = True
                
            i+=1
            
        #Not found any letters?
        if found_at_least_one == False:
            self.wrongly_guessed_letters.append(user_input)
            self.error_count +=1
            self.lives -=1
        print(self.correctly_guessed_letters)

    #Done
    def game_over(self):
       print("game over...")
    

    def start_game(self):
        
        #generating a random number to select a word from the list
        self.word_to_find = self.possible_words[self.random.randint(0,len(self.possible_words)-1)]

        #Setting up the hidden word
        self.correctly_guessed_letters =self.re.sub("[a-z]", "_",self.word_to_find,count=0,flags=0)
        
        #formatting it into a list
        self.correctly_guessed_letters= [*self.correctly_guessed_letters]
        self.word_to_find= [*self.word_to_find]
        
        #to avoid confusion with a temp variable split word to find
        self.word_to_find=self.word_to_find

        while self.word_to_find != self.correctly_guessed_letters:
           
            if self.lives >0:
                
                self.play()
            elif self.lives==0:
                self.game_over()
                break
            if self.word_to_find == self.correctly_guessed_letters:
                self.well_played()
        
        
        #summary of the stats
        #print(f"Correctly guessed letters : {self.correctly_guessed_letters}, wrongly guesssed letters : {self.wrongly_guessed_letters}, life : {self.lives}, error count : {self.error_count}, turn count : {self.error_count} ")
        
    
#TO DO : Doc strings; comment the code
#
#
#TO FIX : do not accept duplicates in wrong answers; maybe convert the char list back to a string
#
#FIXED : Turn_count; game over message
    