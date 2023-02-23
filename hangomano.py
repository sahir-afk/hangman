import random

def hangman(word):
    word = word.lower()
    wrong = 0
    stages = ["",
             "___________________           ",
             "|                             ",
             "|                 |           ",
             "|                 0           ",
             "|                /|\          ",
             "|                / \          ",
             "|                             "]
    rletters = list(word)
    board = ["__ "] * len(word)
    win = False
    print("Welcome to hangman")
    
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Pick a letter ")
        if char in rletters:
            index = rletters.index(char)
            rletters[index] = "*"
            board[index] = char
        else:
            wrong += 1
            stageLen = len(stages)
            stages.pop(stageLen - 2)

        print(" ".join(board))
        print("\n".join(stages))
        
        if("__ " not in board):
            win = True
            print("You Win!!!")
            break

        if len(stages) <= 5:
            print("\nGAME OVER, YOU KILLED HIM!!!!! It was {}!".format(word))
            break
        
words = ["Owl", "City", "Earth", "Princeton", "Rice", "Asleep", "linguistics", "statistics", "economics", "compsci"]       
hangman(random.choice(words))