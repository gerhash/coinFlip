import random #Random module for the choice


#Declaring Const
HEAD = "Head"
TAILS =  "Tails"


#User Class
class User:
    def __init__(self, name, turn): #user Init
        self.name = name #name
        self.choice = None #user choice
        self.score = 0 #init score
        self.turn = turn #useful for turns handling

    def make_choice(self, choice):#transform number choice to String and declare choice
        if choice == 0:
            text_choice = HEAD
        else:
            text_choice = TAILS
        self.choice = text_choice

#Random result coin flip
def coinFlip():
    risultato = random.choice([HEAD, TAILS])
    return risultato

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
def gameLogic(user1, user2,score):
    isPlaying = True #Init the game loop
    while isPlaying == True: #check if the game is on
        print(f"Scores:{user1.name}:{user1.score} | {user2.name}:{user2.score}")

        #turn handling
        if user1.turn == True:
            userChoice = input(f"{user1.name} scegli:\n0)Testa\n1)Croce\n")
            if userChoice == 0:
                user1.make_choice(userChoice)
                user2.make_choice(1)
            elif userChoice == 1:
                    user1.make_choice(userChoice)
                    user2.make_choice(0)
            user1.turn = False
            user2.turn = True
        elif user2.turn == True:
            userChoice = input(f"{user2.name} scegli:\n0)Testa\n1)Croce\n")
            if userChoice == 0:
                user2.make_choice(userChoice)
                user1.make_choice(1)
            elif userChoice == 1:
                user2.make_choice(userChoice)
                user1.make_choice(0)
            user2.turn = False
            user1.turn = True

        result = coinFlip()
        print(f"Coin flipped!")
        turnWinner(result, user1,user2)#check the winner of the turn and scores
        winner = checkWinner(score, user1, user2) #return user object of the winner
        if winner != None:
            print(f"{winner.name} is the Winner!")#print winner name
            isPlaying = False #put  the game off
        else:
            pass #do nothing

#Start Game
def game():

    name1 = input("Insert Username Player 1\n")
    name2 = input("Insert Username Player 2\n")
    score = input("Insert the Winner Score\n")

    #Init Users
    user1 = User(name1, True)
    user2 = User(name2, False)


    gameLogic(user1,user2,score)


#Start Game
game()






