'''Rock Paper Scissors is a hand game, usually played between two people, 
in which each player simultaneously forms one of three shapes with an outstretched handit has three possible outcomes: a draw, a win or a loss. 
A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or "breaks scissors" or 
sometimes "blunts scissors"), but will lose to one who has played paper ("paper covers rock"); 
a play of paper will lose to a play of scissors ("scissors cuts paper").
If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie'''




import random

# Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose r
    elif comp == 'r':
        if you=='p':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose p
    elif comp == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True

print("Comp Turn: Rock(r) Paper(p) or Scissors(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissors(s)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")