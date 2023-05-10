class Hangman:
    """
    A class to represent a hangman.

    Attributes:
        possible_words : List
            List of words to find in the game, only one will be selected
        word_to_find : List
            The selected word to find, formatted to underscores, each element will be replaced
            by the correctly guessed letter.
        lives : Int
            Contains the number of lives the player still has left.
        correctly_guessed_letters : List
            Contains list where each element will be a letter guessed by the user.
        wrongly_guessed_letters : List
            Contains list where each element will be a wrongly guessed letter by the user.
        turn_count : Int
            Contains the number of turns.
        error_count : Int
            Contains the number of wrongly guessed letters by the user.

    """
    import random
    import re


    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    word_to_find = []
    lives = 5
    correctly_guessed_letters = [] 
    wrongly_guessed_letters = []
    turn_count = 0
    error_count = 0

    def __init__(self):
        """
        Function which initializes the class object with all its attributes
        """
        
        self.word_to_find
        self.lives
        self.correctly_guessed_letters
        self.wrongly_guessed_letters
        self.turn_count
        self.error_count
        
    
    def well_played(self):
        """
        Function called when the user has found all the letters in a 
        given word.
        :print: A well played message displaying stats (word the user had to find, number of turns, error count)
        """
        print(f"You found the word : {self.word_to_find}, in  {self.turn_count} turns with {self.error_count} errors!")
    
    
    
    def play(self):
        """
        Main function of the game that will be called after the game has started,
            it is executed in 2 parts:
        1 : Checks the user input if it does not contain more than one character or a number
        2 : Loops through the word to find and checks if the letter given by the user is present
            is present in the word to find.
        
        """

        #----User input----
        #Boolean as a condition to keep the user inside the input loop
        invalid_input = True
        
        # Checks user input and stays in a loop until user complies with the rules.
        print("Please enter a letter")
        while invalid_input:
            
            user_input = str(input())
            #checks if input has more than one character
            if len(user_input) > 1 :
                print("Please enter only one character, retry")

            elif self.re.match('[0-9]| ',user_input):
                print("No numbers or empty characters allowed, retry")

            else:
                #If user complies with the rules, variable is changed to escape the loop
                invalid_input = False
                

        #----Valid character detected----
        #creating a variable that ensures user does not lose points at the end of the loop if found a correct letter
        found_at_least_one = False
        self.turn_count += 1

        #creating an index variable to ease 
        i = 0

        #Loop through the word to find to compare each letters
        for letter in self.word_to_find:
            
            if letter == user_input:
                self.correctly_guessed_letters[i] = letter
                #Bool var to not lose lives if found letter
                found_at_least_one = True
                
            i += 1
            
        #Not found any letters
        if found_at_least_one == False:
            self.wrongly_guessed_letters.append(user_input)
            self.error_count += 1
            self.lives -= 1

        print(self.correctly_guessed_letters)

    
    def game_over(self):
       """
       Function called when the user has no more lives, it stops the game.
       :print: Game over message
       """
       print("game over...")
    

    def start_game(self):
        """
        Function that will call all the other functions in the code, it is executed in 2 parts:
        1 : Picks the word to find at random
        2 : Copies the list word to find and to a new list of correctly guessed words
            and replaces all its characters with underscore.
        3 : Runs a while loop, the game is going on as long as the user has not found
            the correct word or user runs out of lives and calls the adequate function.
            
        """
        
        #generating a random number that will be used as an Index to select a word from the list
        """"""""
        self.word_to_find = Hangman.possible_words[self.random.randint(0 , len(Hangman.possible_words)-1)]

        #Setting up the hidden word
        self.correctly_guessed_letters = self.re.sub("[a-z]" , "_" , self.word_to_find, count = 0, flags = 0)
        
        #formatting it into a list of characters
        self.correctly_guessed_letters = list(self.correctly_guessed_letters)
        self.word_to_find = list(self.word_to_find)
        
        #to avoid confusion with a temp variable split word to find
        self.word_to_find = self.word_to_find

        #Game loop
        while self.word_to_find != self.correctly_guessed_letters:
           
            if self.lives > 0 :
                self.play()

            elif self.lives == 0 :
                self.game_over()
                break

            if self.word_to_find == self.correctly_guessed_letters:
                self.well_played()

    