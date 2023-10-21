import random

# get all words from textfile to list
def loadWordSet(path: str):
    word_lst = []
    with open(path, "r") as file:
        for line in file.readlines():
            word = line.strip().upper()
            word_lst.append(word)
    return word_lst

# pick random word from list
def getRandomWord(wordset):
    return random.choice(list(wordset))

# display border + result on terminal
def drawBorder(lines, size=9, pad=1):
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)
    for line in lines:
        print("│" + space + line + space + "│")
    print(bottom_border)

# display result (or _ _ _ _ _) on terminal
def displayResult(wordle: Wordle):
    print(f"You have {wordle.remainingAttempts()} attempts left.")

    lines = []
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convertWord2Color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remainingAttempts()):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH)) # _ _ _ _ _

    drawBorder(lines)
    
    
if __name__ == "__main__":
    main()
