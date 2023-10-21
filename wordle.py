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