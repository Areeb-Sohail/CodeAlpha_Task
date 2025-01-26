import random

hint ={"python":"Popular progrmmaing language in Data Science & Artificial Intelligence", 
       "java":"A Backward capatible programming language", 
       "javascript":"A popular programming language for web development", 
       "hangman":"The game name", 
       "computer":"A sophisticated device wich can compute information and data in precidented speed", 
       "programming":"Feeding instructions tom computer", 
       "developer":"An individual that develops ", 
       "algorithm":"A step by step solution to a problem"
       }
def choose_word():
    word_list = ["python", "java", "javascript", "hangman", "computer", "programming", "developer", "algorithm"]
    return random.choice(word_list)

def display_board(hidden_word, guessed_letters, attempts_left):
    print("\nCurrent word: ", " ".join(hidden_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")

def hangman():
    word = choose_word()
    hidden_word = ['_'] * len(word)
    guessed_letters = []
    attempts_left = 6  # You can adjust this to give more/less attempts
    guessed = False
    
    while attempts_left > 0 and not guessed:
        display_board(hidden_word, guessed_letters, attempts_left)
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed {guess}. Try again!")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good job! {guess} is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word[i] = guess
        else:
            attempts_left -= 1
            print(f"Oops! {guess} is not in the word.")
        
        if "_" not in hidden_word:
            guessed = True
            print("\nCongratulations! You guessed the word:", word)
        if attempts_left == 1:
            print(f'\nHint: {hint[word]}')
    
    if attempts_left == 0:
        print("\nGame over! You ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
