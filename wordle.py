from letter_state import LetterState

class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    
    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.attempts = []

    # Store User Attempted Words in List
    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
    
    # Check if the Player has won or not
    def gameWin(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    # Count the number of attempts remaining for the Player
    def remainingAttempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)
    
    # Validate the number of attempts for Player 
    def stillAttempt(self):
        return self.remainingAttempts() > 0 and not self.gameWin()
    
    # Validate User Guesses
    def guess(self, word: str):
        word = word.upper()
        # convert the word to a list
        remaining_secret = list(self.secret)

        # Initialize the results array
        result = []
        for char in word:
            result.append(LetterState(char))

        # Check for Green Letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.in_right_position = True
                remaining_secret[i] = '*'

        # Check for Yellow Letters
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            # skip the letters if they are in the right place
            if letter.in_right_position:
                continue
        
            # Otherwise check if the letter is in the word, and void the index
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = '*'
                    letter.in_word = True
                    break
        return result