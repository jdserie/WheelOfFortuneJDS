import getpass
import os

os.system("cls||clear")

guide = [
    {'letter':' ','point':0},
    {'letter':"'",'point':0},
    {'letter':"-",'point':0},
    {'letter':'A','point':1},
    {'letter':'B','point':4},
    {'letter':'C','point':4},
    {'letter':'D','point':2},
    {'letter':'E','point':1},
    {'letter':'F','point':4},
    {'letter':'G','point':3},
    {'letter':'H','point':3},
    {'letter':'I','point':1},
    {'letter':'J','point':10},
    {'letter':'K','point':5},
    {'letter':'L','point':2},
    {'letter':'M','point':4},
    {'letter':'N','point':2},
    {'letter':'O','point':1},
    {'letter':'P','point':4},
    {'letter':'Q','point':10},
    {'letter':'R','point':1},
    {'letter':'S','point':1},
    {'letter':'T','point':1},
    {'letter':'U','point':2},
    {'letter':'V','point':5},
    {'letter':'W','point':4},
    {'letter':'X','point':8},
    {'letter':'Y','point':3},
    {'letter':'Z','point':10}
]


def print_board():
    tmp = ""
    for i in board:
        tmp += f"{i} "
    print(tmp)


def make_guess():
    counter = 0
    global guess_wrong
    option = input("Do you want to guess the puzzle? y/n\n>")
    if option == 'n':
        guess = input("Guess a letter: ").upper()
        if guess in guess_wrong:
            print("The letter has already been chosen!")
        else:
            if guess in word:
                for i in word:
                    if i == guess:
                        board[counter] = guess
                    counter += 1
                if "_" not in board:
                    print_board()
                    os.system("cls||clear")
                    print("Challenger, you figured it out: " + word)
                    print("You Win!")
                    print("You earned " + total_str + " points!")
                    exit()
            else:
                guess_wrong += f" {guess}"
                global trys
                trys -= 1
                if trys == 0:
                    os.system("cls||clear")
                    print("The answer was: " + word)
                    print("Host Player Wins!")
                    print("You earned " + total_str_host + " points!")
                    quit()
    elif option == 'y':
        guess_answer = input("Guess the answer: ").upper()
        if guess_answer == word:
            os.system("cls||clear")
            print("Challenger, you guessed right: " + word)
            print("You Win!")
            print("You earned " + total_str + " points!")
            quit()
        elif guess_answer != word:
            trys -= 1
            if trys > 0:
                print("You guessed incorrectly!")
            else:
                os.system("cls||clear")
                print("The answer was: " + word)
                print("Host Player Wins!")
                print("You earned " + total_str_host + " points!")
                quit()


def make_space_guess():
    counter = 0
    if " " in word:
        for i in word:
            if i == " ":
                board[counter] = " "
            counter += 1


def make_special_guess():
    counter = 0
    if "'" in word:
        for i in word:
            if i == "'":
                board[counter] = "'"
            counter += 1

def make_special_guess_2():
    counter = 0
    if "-" in word:
        for i in word:
            if i == "-":
                board[counter] = "-"
            counter += 1


v = getpass.getpass("(ONLY USE: Letters, Dashes, Spaces, and Apostraphes)\nEnter the phrase/word for the puzzle: ")
word = v.upper()
cat = input("What is the Category?\n> ")
list_word = list(word)
total = 0
for i in word:
    for x in guide:
        if x['letter'] == i:
            total += x['point']

total_str = str(total)
total_str_host = str(45 - total)
board = []
trys = 6
guess_wrong = ""

for i in word:
    board.append("_")

make_space_guess()
make_special_guess()
make_special_guess_2()
while True:
    tx = f"Tries left: {trys} "
    if guess_wrong:
        tx += f"\nLetters you have tried: {guess_wrong}"
    os.system("cls||clear")
    print("Category: " + cat + "\n" + tx)
    print_board()
    make_guess()
