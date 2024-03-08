import random

#Declaring Const
HEAD = "Head"
TAILS =  "Tails"

#User Class
class User:
    def __init__(self, name, turn):
        self.name = name
        self.choice = None
        self.score = 0
        self.turn = turn

    def make_choice(self, choice):
        if choice == 0:
            text_choice = HEAD
        else:
            text_choice = TAILS
        self.choice = text_choice

#Random result coin flip
def coinFlip():
    result = random.choice([HEAD, TAILS])
    return result

#This function check the winner of turn, handling the score
def turnWinner(result, user1, user2):
    print(f"Coin result is: {result}")
    if user1.choice == result:
        user1.score += 1
        print(f"{user1.name} scored Point!")
    else:
        user2.score += 1
        print(f"{user2.name} scored Point!")

#This function checks the winner comparing his User Object score with the declared score in the init
def checkWinner(score, user1, user2):
    if user1.score == score:
        return user1
    elif user2.score == score:
        return user2
    else:
        return None

#Game logics
def gameLogic(user1, user2, score):
    isPlaying = True
    while isPlaying:
        print(f"Scores: {user1.name}: {user1.score} | {user2.name}: {user2.score}")

        #turn handling
        if user1.turn:
            while True:
                try:
                    userChoice = int(input(f"{user1.name}'s choice:\n0) Head\n1) Tails\n"))
                    if userChoice not in [0, 1]:
                        raise ValueError("Invalid choice. Please enter 0 or 1.")
                    break
                except ValueError as e:
                    print(e)
            user1.make_choice(userChoice)
            user2.make_choice(1 - userChoice)
            user1.turn = False
            user2.turn = True
        elif user2.turn:
            while True:
                try:
                    userChoice = int(input(f"{user2.name}'s choice:\n0) Head\n1) Tails\n"))
                    if userChoice not in [0, 1]:
                        raise ValueError("Invalid choice. Please enter 0 or 1.")
                    break
                except ValueError as e:
                    print(e)
            user2.make_choice(userChoice)
            user1.make_choice(1 - userChoice)
            user2.turn = False
            user1.turn = True

        result = coinFlip()
        print("Coin flipped!")
        turnWinner(result, user1, user2)
        winner = checkWinner(score, user1, user2)
        if winner is not None:
            print(f"{winner.name} is the Winner!")
            isPlaying = False
        else:
            pass

#Start Game
def game():
    name1 = input("Insert Username Player 1\n")
    name2 = input("Insert Username Player 2\n")
    while True:
        try:
            score = int(input("Insert the Winner Score\n"))
            if score <= 0:
                raise ValueError("Score must be a positive integer.")
            break
        except ValueError as e:
            print(e)

    #Init Users
    user1 = User(name1, True)
    user2 = User(name2, False)

    gameLogic(user1, user2, score)

#Start Game
game()
